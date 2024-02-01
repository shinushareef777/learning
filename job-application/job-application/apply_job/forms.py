from django import forms
from django.forms import ModelForm, ValidationError
from django import forms
from .models import JobApplication
from datetime import date, datetime

# main form form the project
class ApplicationForm(ModelForm):

    # Meta class to get all the fields from the
    class Meta:
        # setting the form model as the JobApplication model
        model = JobApplication
        # excluding the date_applied field from the application form
        # and show every other field in the application form
        exclude = ["date_applied"]
        # widget to render gender as radio buttons
        widgets = {"gender": forms.RadioSelect()}

    # Adding attritubetes to the model form for styling and how to view it html
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].label = "First Name"
        self.fields["first_name"].widget.attrs.update(
            {
                "class": "text fn",
                "placeholder": "Enter your First Name",
                "onchange": "return nameValidation('fn')",
                "oninput": "return nameValidation('fn')",
                "onblur": "return nameValidation('fn')",
            }
        )
        self.fields["last_name"].label = "Last Name"
        self.fields["last_name"].widget.attrs.update(
            {
                "class": "text ln", 
                "placeholder": "Enter your Last Name", 
                "onchange": "return nameValidation('fn')"
            }
        )
        self.fields["email"].label = "Email"
        self.fields["email"].widget.attrs.update(
            {   
                "class": "text em",
                "placeholder": "Enter your Email Address",
                "oninput": "return validateEmail('em')",
                "onchange": "return validateEmail('em')",
                "onblur": "return validateEmail('em')",
            }
        )
        self.fields["phone_number"].label = "Phone Number"
        self.fields["phone_number"].widget.attrs.update(
            {
                "class": "text ph",
                "placeholder": "Enter your Mobile Number",
                "oninput": "return validatePhoneNumber('ph')",
                "onblur": "return validatePhoneNumber('ph')",
                "onchange": "return validatePhoneNumber('ph')",
            }
        )
        self.fields["position_applying"].label = "Position Applying"
        self.fields["position_applying"].widget.attrs.update(
            {"class": "text pa", "placeholeder": "select the position"}
        )
        self.fields["date_of_birth"].label = "Date of Birth"
        self.fields["date_of_birth"].widget.input_type = "date"
        self.fields["date_of_birth"].widget.attrs.update(
            {
                "class": "text dob",
                "oninput": "validateDateofBirth('dob')",
                "placeholder": "dd/mm/yy",
            }
        )
        self.fields["experience"].label = "Experience"
        self.fields["experience"].widget.attrs.update({"class": "text ex"})

        self.fields["gender"].label = "Gender"
        self.fields["gender"].widget.attrs.update(
            {"class": "textge ge", "type": "radio"}
        )
        self.fields["address"].label = "Address"
        self.fields["address"].widget.attrs.update(
            {"class": "text ad", "placeholder": "Enter your Address", "id": "texta"}
        )
        self.fields["city"].label = "City"
        self.fields["city"].widget.attrs.update(
            {"class": "text ct", "placeholder": "Enter your City"}
        )
        self.fields["nationality"].label = "Nationality"
        self.fields["nationality"].widget.attrs.update(
            {"class": "text nl", "placeholder": "Enter your Nationality"}
        )
        self.fields["expected_ctc"].label = "Expected CTC"
        self.fields["expected_ctc"].widget.attrs.update(
            {"class": "text fn", "placeholder": "Enter your Expected CTC"}
        )
        self.fields["current_ctc"].label = "Current CTC"
        self.fields["current_ctc"].widget.attrs.update(
            {"class": "text fn", "placeholder": "Enter your Current CTC"}
        )
        self.fields["github_url"].label = "Github URL"
        self.fields["github_url"].widget.attrs.update(
            {"class": "text gh", "placeholder": "Enter your Github URL"}
        )
        self.fields["linkedin_url"].label = "LinkedIn URL"
        self.fields["linkedin_url"].widget.attrs.update(
            {"class": "text ln", "placeholder": "Enter your LinkedIn URL"}
        )

    # helper function to avoid repetition
    def _helper(self, val, text):
        if val == "":
            raise ValidationError(f"You should enter your {text}")

    # validation for first name
    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if first_name == "":
            raise ValidationError("You should Enter your name")
        if len(first_name) < 3 or len(first_name) > 25 :
            raise ValidationError("First Name must between 3 and 25 characters")
        return first_name

    # Validating if last name is empty
    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        self._helper(last_name, "Last Name")
        return last_name

    # Validating if email is empty
    def clean_email(self):
        email = self.cleaned_data["email"]
        self._helper(email, "Email")
        return email

    # Validating if phone number  is empty
    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        self._helper(phone_number, "Phone Number")
        return phone_number

    # Validating if address is empty
    def clean_address(self):
        address = self.cleaned_data["address"]
        self._helper(address, "Address")
        return address

    # Validating if last name is empty
    def clean_gender(self):
        gender = self.cleaned_data["gender"]
        self._helper(gender, "Gender")
        return gender

    # Validating if city is empty
    def clean_city(self):
        city = self.cleaned_data["city"]
        self._helper(city, "City")
        return city

    # Validating if nationality is empty
    def clean_nationality(self):
        nationality = self.cleaned_data["nationality"]
        self._helper(nationality, "Nationality")
        return nationality

    # Validating if experience is empty
    def clean_experience(self):
        experience = self.cleaned_data["experience"]
        self._helper(experience, "Experience ")
        return experience

    # Validating if position applying  is empty
    def clean_position_applying(self):
        position_applying = self.cleaned_data["position_applying"]
        if position_applying is None:
            raise ValidationError("You should add the position applying")
        return position_applying

    # Validating if Expected ctc is empty
    def clean_expected_ctc(self):
        expected_ctc = self.cleaned_data["expected_ctc"]
        self._helper(expected_ctc, "Expected CTC")
        return expected_ctc

    # Validating if Current ctc is empty
    def clean_current_ctc(self):
        current_ctc = self.cleaned_data["current_ctc"]
        self._helper(current_ctc, "Current CTC")
        return current_ctc

    # Validating if DOB is empty and age is > 18
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data["date_of_birth"]
        today = date.today()
        try:
            age = (today - date_of_birth).days / 365
        except TypeError:
            raise ValidationError("You should enter your Date of Birth")
        if age < 18 or age > 90:
            raise ValidationError("You must be aged 18 or above to apply for this job")
        return date_of_birth
