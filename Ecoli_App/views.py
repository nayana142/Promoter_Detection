from django.shortcuts import render
from django.http import HttpResponse
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from django.shortcuts import redirect
import tensorflow.keras as keras
from tensorflow import keras
from .forms import DNASequenceForm
from .models import DNASequence
import tensorflow as tf

def index(request):
    return render(request, 'index.html')

def input_sequence(request):
    if request.method == 'POST':
        form = DNASequenceForm(request.POST)
        if form.is_valid():
            sequence = form.cleaned_data['sequence']
            data = pd.DataFrame({'Sequence': sequence}, index=[range(0,1)])

            # reshaped_sequence = np.array(sequence).reshape(1, -1)
            split_data = data['Sequence'].str.split('', expand=True)
            # Drop columns 0 and 58
            split_data.drop(columns=[0, 58], inplace=True)
            # Rename columns from 0 to 57
            new_column_names = [str(i) for i in range(0, 57)]
            split_data.columns = new_column_names

            one_hot_encoder = pickle.load(open('final_encoder1.pkl', 'rb'))
            promoter_model = pickle.load(open('final_Model1.pkl', 'rb')) 
            encoded_sequence = one_hot_encoder.transform(split_data)
            # Make predictions using the loaded model

            prediction = promoter_model.predict(encoded_sequence)
            affected_by_ecoli = prediction > 0.5  # Example threshold for binary classification
            sequence = form.save(commit=False)
            sequence.affected_by_ecoli = affected_by_ecoli
            sequence.save()
            return redirect('result')
    else:
        form = DNASequenceForm()
    return render(request, 'input.html', {'form': form})

# def result(request, pk):
#     sequence = DNASequence.objects.get(pk=pk)
#     return render(request, 'result.html', {'sequence': sequence})

def result(request):
    # Retrieve the current DNA sequence from the database
    current_sequence = DNASequence.objects.first()
    return render(request, 'result.html', {'current_sequence': current_sequence})

def previous_results(request):
    # Retrieve all DNA sequences from the database
    dna_sequences = DNASequence.objects.all()

    # Convert DNA sequences to a DataFrame
    data = []
    for sequence in dna_sequences:
        data.append({
            'Sequence': sequence.sequence,
            'Affected by E.coli': "Yes" if sequence.affected_by_ecoli else "No",
            'Created Date': sequence.created_at
        })
    df = pd.DataFrame(data)

    return render(request, 'previous_results.html', {'previous_sequences': df})
