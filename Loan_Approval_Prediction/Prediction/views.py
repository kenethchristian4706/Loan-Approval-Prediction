from django.shortcuts import render
import numpy as np
from joblib import load
import os

MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'loan_approval_prediction.joblib')

model = load(MODEL_PATH)

def loan_form(request):
    result = None
    if request.method == 'POST':
        try:
            # Get form data
            income_annum = float(request.POST.get('income_annum'))
            loan_amount = float(request.POST.get('loan_amount'))
            loan_term = float(request.POST.get('loan_term'))
            cibil_score = float(request.POST.get('cibil_score'))
            residential_assets_value = float(request.POST.get('residential_assets_value'))
            commercial_assets_value = float(request.POST.get('commercial_assets_value'))
            luxury_assets_value = float(request.POST.get('luxury_assets_value'))
            bank_asset_value = float(request.POST.get('bank_asset_value'))
            # Prepare input for model (no scaling)
            input_data = np.array([
                income_annum,
                loan_amount,
                loan_term,
                cibil_score,
                residential_assets_value,
                commercial_assets_value,
                luxury_assets_value,
                bank_asset_value
            ]).reshape(1, -1)
            prediction = model.predict(input_data)[0]
            result = 'Approved' if prediction == 1 else 'Rejected'
        except Exception as e:
            result = f'Error: {str(e)}'
    return render(request, 'Prediction/loan_form.html', {'result': result})
