from django import forms



class HousesFilterForm(forms.Form):
    min_price = forms.IntegerField(label="от", required=False)
    max_price = forms.IntegerField(label="до", required=False)
    ordering = forms.ChoiceField(label="Сортировка", required=False, choices=[
        ["name", "по алфавиту"],
        ["price", "дешевые сверху"],
        ["-price", "дорогие сверху"]
    ])

