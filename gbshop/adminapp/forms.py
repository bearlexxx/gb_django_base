from django import forms
from authapp.models import ShopUser
from authapp.forms import ShopUserEditForm
from django.db import connection
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from productsapp.models import ProductCategory, Product

from productsapp.views import db_profile_by_type


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'


class ProductCategoryEditForm(forms.ModelForm):
    discount = forms.IntegerField(label='скидка', required=False, min_value=0, max_value=90, initial=0)

    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductCategoryEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ProductCategoryUpdateView(UpdateView):
   model = ProductCategory
   template_name = 'adminapp/category_update.html'
   success_url = reverse_lazy('admin:categories')
   form_class = ProductCategoryEditForm

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['title'] = 'категории/редактирование'
       return context

   def form_valid(self, form):
       if 'discount' in form.cleaned_data:
           discount = form.cleaned_data['discount']
           if discount:
               self.object.product_set. \
                   update(price=F('price') * (1 - discount / 100))
               db_profile_by_type(self.__class__, 'UPDATE', connection.queries)

       return super().form_valid(form)


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

