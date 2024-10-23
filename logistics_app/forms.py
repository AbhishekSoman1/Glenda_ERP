
from django import forms
from logistics_app.models import Driver, Route, Route_Plan, Vehicle



class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['driver_name' ,'license_number' ,'aadhaar_number' ,'phone_number']
        widgets = {
            'driver_name' :forms.TextInput(attrs={'class' :'form-control'}),
            'license_number' :forms.TextInput(attrs={'class' :'form-control'}),
            'aadhaar_number' :forms.TextInput(attrs={'class' :'form-control'}),
            'phone_number' :forms.TextInput(attrs={'class' :'form-control'}),
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_name' ,'vehicle_nbr' ,'vehicle_img']
        widgets = {
            'vehicle_name' :forms.TextInput(attrs={'class' :'form-control'}),
            'vehicle_nbr' :forms.TextInput(attrs={'class' :'form-control'}),
            'vehicle_img' :forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
# forms.py

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['route_name','starting_point','ending_point','total_distance']
        widgets = {
            'route_name': forms.TextInput(attrs={'class': 'form-control'}),
            'starting_point': forms.TextInput(attrs={'class': 'form-control'}),
            'ending_point': forms.TextInput(attrs={'class': 'form-control'}),
            'total_distance': forms.TextInput(attrs={'class': 'form-control'}),

        }

class RoutePlanForm(forms.ModelForm):
    class Meta:
        model = Route_Plan
        fields = ['vehicle', 'route', 'driver', 'date', 'time']
        widgets = {
            'vehicle': forms.Select(attrs={'class': 'form-control'}),
            'route': forms.Select(attrs={'class': 'form-control', 'id': 'id_route'}),
            'driver': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

    # Fields for route details
    route_distance = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control', 'placeholder': 'Route Distance'})
    )
    route_starting_point = forms.CharField(  # Updated field name
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control', 'placeholder': 'Starting Destination'})
    )
    route_ending_point = forms.CharField(  # Updated field name
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control', 'placeholder': 'Ending Destination'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['route_distance'].initial = ''
        self.fields['route_starting_point'].initial = ''  # Updated field name
        self.fields['route_ending_point'].initial = ''  # Updated field name

        if 'route' in self.data:
            try:
                route_id = int(self.data.get('route'))
                route = Route.objects.get(id=route_id)
                self.fields['route_distance'].initial = route.total_distance  # Matches model field
                self.fields['route_starting_point'].initial = route.starting_point  # Matches model field
                self.fields['route_ending_point'].initial = route.ending_point  # Matches model field
            except (ValueError, Route.DoesNotExist):
                pass

