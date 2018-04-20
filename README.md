# bsmsg
Bootstrap Messages using the builtin Django messages framework

## Installation
Install it using pip
```
pip install git+https://github.com/lzantal/bsmsg.git
```

## Usage
Add bsmsg to your INSTALLED_APPS in settings.py
```
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #
    'bsmsg',
    ...
)
```

Load the bsmsg template tag in your html file Eg: base.html
```
{% load bsmsg %}
```
Then add it to your template
```
{% bsmsg %}
```

## Optional
Include the bsmsg.css file to center text, make it bolder and larger
```
<link href="{% static 'css/bsmsg.css' %}" rel="stylesheet">
```

## Custom Styles
message boxes wrapped around with a div using the ID **#bsmsg**  
Use it to over write any other styles
