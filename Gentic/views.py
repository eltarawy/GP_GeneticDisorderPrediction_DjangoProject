from django.shortcuts import render, redirect
import numpy as np
from django.conf import settings
from django.contrib.auth.decorators import login_required 
import joblib 
model_path1 = settings.BASE_DIR / 'MLModel/genetic disorder final.pkl'
model_path2 = settings.BASE_DIR / 'MLModel/disorder_Subclass final.pkl'
# Load the first model
model1 = joblib.load(model_path1)
# Load the second model
model2 = joblib.load(model_path2)

# Create your views here.
@login_required
def prediction(request):
    return render(request, 'Gentic/prediction.html')

@login_required
def geno_prediction(request):
    l1 = 0
    l2 = 0
    m1 = 0
    m2 = 0
    p1 = 0
    p2 = 0
    p3 = 0
    q1 = 0
    q2 = 0
    q3 = 0
    u1 = 0
    u2 = 0
    u3 = 0
    u4 = 0
    # global l1, l2, m1, m2, p1, p2, p3, q1, q2, q3, u1, u2, u3, u4
    if request.method == 'POST':
        a = request.POST['a']   #patient Age?
        b = request.POST['b']   #blood cell count (mcl)?
        c = request.POST['c']   #white blood cell count(thousand per microliter)?
        e = request.POST['e']   #Is the gene present in the mother's side?
        f = request.POST['f']   #Is the gene present in the father's side?
        g = request.POST['g']   #Is gene present in patients' mother side of the family?
        h = request.POST['h']   #Is gene present in patients'father side of family?
        i = request.POST['i']   #>Respiratory rate?
        j = request.POST['j']   #Heart rate?
        k = request.POST['k']   #What is the patient level of risk?
        l = request.POST['l']   #>Gender?
        if l == 'Female':
            l1 = 1
            l2 = 0
        elif l == 'Male':
            l1 = 0
            l2 = 1
        elif l == 'I perfer not to answer':
            l1 = 0
            l2 = 0
        m = request.POST['m']   #Did the patient experience asphyxia during childbirth
        if m == 'No':
            m1 = 1
            m2 = 0
        elif m == 'Yes':
            m1 = 0
            m2 = 1
        elif m == 'Not available':
            m1 = 0
            m2 = 0
        n = request.POST['n']   #Folic acid test?
        o = request.POST['o']   #H/O Maternal illness?
        p = request.POST['p']   #H/O radition exposure?
        if p == 'No':
            p1 = 1
            p2 = 0
            p3 = 0
        elif p == 'Not aplicable':
            p1 = 0
            p2 = 1
            p3 = 0
        elif p == 'Yes':
            p1 = 0
            p2 = 0
            p3 = 1
        q = request.POST['q']   #Not aplicable --> H/O substantce abuse?
        if q == 'No':
            q1 = 1
            q2 = 0
            q3 = 0
        elif q == 'Not aplicable':
            q1 = 0
            q2 = 1
            q3 = 0
        elif q == 'Yes':
            q1 = 0
            q2 = 0
            q3 = 1
        r = request.POST['r']   #is there assisted conception?
        s = request.POST['s']   #H/O Previous pregnancies?
        t = request.POST['t']   #Birth defects?
        u = request.POST['u']   #blood test result?
        if u == 'Inconclusive':
            u1 = 1
            u2 = 0
            u3 = 0
            u4 = 0
        elif u == 'Normal':
            u1 = 0
            u2 = 1
            u3 = 0
            u4 = 0
        elif u == 'Slightly Abnormal':
            u1 = 0
            u2 = 0
            u3 = 1
            u4 = 0
        elif u == 'Abnormal':
            u1 = 0
            u2 = 0
            u3 = 0
            u4 = 1

        input_data1 = np.array([[a, b, c, e, f, g, h, i,
                                 j, k, l1, l2, m1, m2, n, o, p1, p2, p3, q1, q2, q3, r, s, t, u1, u2, u3, u4]])
        print( input_data1)
        
        # result of the first model
        result1 = model1.predict(input_data1)
        result1 = float(result1)
        print( result1 )

        input_data2 = np.array([[a, b, c, result1, e, f, g, h, i,
                                 j, k, l1, l2, m1, m2, n, o, p1, p2, p3, q1, q2, q3, r, s, t, u1, u2, u3, u4]])
        print( input_data2 )

        # result of the second model
        result2 = model2.predict(input_data2)
        result2 = float(result2)
        print( result2 )

        return render(request, 'Gentic/geno_prediction.html', {'result1': result1, 'result2': result2})
    else:
        return redirect('home')
