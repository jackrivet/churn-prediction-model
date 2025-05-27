from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.regularizers import l1
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import classification_report
from sklearn.calibration import CalibratedClassifierCV
from sklearn.isotonic import IsotonicRegression

def build_model(input_dim):
    model = Sequential([
        Dense(64, activation='relu', input_dim=input_dim, kernel_regularizer=l1(0.015)),
        Dropout(0.4),
        Dense(64, activation='relu', kernel_regularizer=l1(0.015)),
        Dropout(0.4),
        Dense(64, activation='relu', kernel_regularizer=l1(0.015)),
        Dense(1)
    ])

    model.compile(optimizer=Adam(learning_rate=0.0000525), loss='binary_crossentropy', metrics=['accuracy'])
    return model
  
def run_model_pipeline(df):
    termination_cols = [c for c in df.columns if 'Termination' in c]
  
    df['target'] = df[termination_cols].notnull().any(axis=1).astype(int)
    id_col = df['Id']
  
    X = pd.get_dummies(df.drop(termination_cols + ['target', 'Id'], axis=1).fillna('Null'))
    y = df['target']

    X_train, X_test, y_train, y_test, id_train, id_test = train_test_split(X, y, id_col, test_size=0.4, random_state=42)

    X_train, y_train = SMOTE().fit_resample(X_train, y_train)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = build_model(X_train_scaled.shape[1])
    model.fit(X_train_scaled, y_train, epochs=150, batch_size=55, validation_data=(X_test_scaled, y_test), verbose=1)

    raw_probs = model.predict(X_test_scaled).flatten()
    iso_reg = IsotonicRegression(out_of_bounds='clip')
    iso_reg.fit(raw_probs, y_test)
    calibrated = iso_reg.predict(raw_probs)
  
    return model, iso_reg, X_test, y_test, calibrated, id_test
