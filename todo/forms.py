from django import forms

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
        )
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Task
        fields = "__all__"

    def clean_tags(self):
        tags = self.cleaned_data["tags"]
        if not tags:
            raise forms.ValidationError("Select at least one tag")
        return tags


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
