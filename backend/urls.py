from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from backend.views import PartnerUpdate, RegisterAccount, LoginAccount, CategoryView, ShopView, ProductInfoView, \
    BasketView, AccountDetails, ContactView, OrderView, PartnerState, PartnerOrders, ConfirmAccount

app_name = 'backend'
urlpatterns = [
    path('user/register', AccountRegister.as_view(), name='user-register'),
    path('user/register/confirm', AccountConfirm.as_view(), name='user-register-confirm'),
    path('user/login', AccountLogin.as_view(), name='user-login'),
    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('partner/', Uploadsmt.as_view(), name='goods-update'),
    path('products',ProductInfoView.as_view(), name='shops'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders')
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('shops', ShopView.as_view(), name='shops'),
    path('accounts/', include('allauth.urls')),
]
