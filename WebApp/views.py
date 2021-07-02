from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


# Create your views here.


def index(requests):
    return render(requests, 'index.html')

def stories(requests):
    response = render(requests, 'stories.html')  
    if requests.method == 'POST':
        try:  # file uploading, if user has clicked on video, then the file upload will give error and go to except loop
            uploaded_file = requests.FILES['document']
            print(uploaded_file.name,uploaded_file.size)
            fs = FileSystemStorage()
            fs.save(uploaded_file.name,uploaded_file)
            messages.success(requests,"Thank you for sharing your experience!")
            response = render(requests, 'stories.html') 
        except: # video name
            # print('Video name',requests.POST.get('video1'),requests.POST.get('video2'),requests.POST.get('video3'))
            if 'video1' in requests.POST:
                print("video1")
                url = requests.POST.get('video_1')   
            elif 'video2' in requests.POST:
                print("video2")
                url = requests.POST.get('video_2')
            elif 'video3' in requests.POST:
                print("video3")
                url = requests.POST.get('video_3')
            elif 'video4' in requests.POST:
                print("video4")
                url = requests.POST.get('video_4')
            elif 'video5' in requests.POST:
                print("video5")
                url = requests.POST.get('video_5')
            else:
                print("Else")
                url= None
            print(url)
            response = render(requests, 'stories.html',{'url':url}) 
    return response


def information(requests):
    return render(requests, 'information.html') 


def about_us(requests):
    return render(requests, 'about_us.html') 

def contact_us(requests):
    print("Contact us")
    if requests.method == 'POST':   # is it a post request
        first_name = requests.POST.get('first_name')
        last_name = requests.POST.get('last_name')
        email_address = requests.POST.get('email_address')
        password = requests.POST.get('password')
        address = requests.POST.get('address')
        city = requests.POST.get('city')
        state = requests.POST.get('state')
        zip = requests.POST.get('zip')
        gender_male = requests.POST.get('gender_male')
        gender_female = requests.POST.get('gender_female')
        print(first_name,last_name,email_address,password,address,city,state,zip,gender_male,gender_female)
        messages.success(requests, 'The form has been successfully submitted!!!') 
    return render(requests, 'contact_us.html') 


def appointment(requests):
    return render(requests, 'appointment.html')




