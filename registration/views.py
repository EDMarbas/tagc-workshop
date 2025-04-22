# registration/views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration

def register(request):
    submitted = False
    form = RegistrationForm() # Initialize form outside the if/else

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                # Check if email already exists *before* saving if unique=True isn't enough
                # Or handle potential IntegrityError during save if using unique=True
                registration_obj = form.save() # Save and get the object instance
                # Store the ID of the newly created registration in the session
                request.session['registration_id'] = registration_obj.id
                submitted = True # Set flag to display thank you message
                # Important: Re-instantiate the form *after* successful POST
                # if you want to show an empty form below thank you, but here we show thank you message instead
                # form = RegistrationForm() # Creates a fresh empty form
            except Exception as e: # Catch potential errors (like duplicate email if unique=True)
                 # Handle errors, maybe log them or add a general form error
                 print(f"Error saving registration: {e}") # Log error for debugging
                 # Example: Add a non-field error
                 form.add_error(None, "An error occurred during registration. Please try again or contact support if the problem persists.")


    context = {
        'form': form,
        'submitted': submitted,
        # Note: 'request' is automatically available in templates if using RequestContext
        # but explicitly passing session data might be needed if not using it.
        # Django's default render shortcut uses RequestContext.
    }
    return render(request, 'registration/register.html', context)

# View for the profile page (add this new function)
def profile(request):
    registration_id = request.session.get('registration_id', None) # Get ID from session
    registration_details = None
    error_message = None

    if registration_id:
        try:
            registration_details = Registration.objects.get(pk=registration_id)
        except Registration.DoesNotExist:
            error_message = "Your registration details could not be found. It might be from a previous session."
            # Optionally clear the invalid ID from the session
            # del request.session['registration_id']
    else:
        error_message = "You have not registered during this session. Please register first."

    context = {
        'registration': registration_details,
        'error_message': error_message,
    }
    return render(request, 'registration/profile.html', context)


def home(request):
  
  return render(request, 'registration/home.html')