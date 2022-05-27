from django.shortcuts import render
from core.utils import process_automobile_data
from core.decorators import admin_only


@admin_only
def build_automobile_dataframe(request, segment):
    df = process_automobile_data(segment)
    print(df.to_html())
    return render(request, 'repair_shops/index.html')
