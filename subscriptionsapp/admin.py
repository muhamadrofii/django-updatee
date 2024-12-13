from django.contrib import admin
from subscriptionsapp.models import Transaction, Subscription

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'email', 'plan', 'amount', 'status', 'created_at', 'user' )
    list_filter = ('status', 'plan', 'created_at')
    search_fields = ('order_id', 'user__username', 'profile__user__username', 'full_name')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'status', 'start_date', 'end_date', 'created_at')
    list_filter = ('status', 'plan')
    search_fields = ('user__username', 'plan')  # Cari berdasarkan username atau plan
    ordering = ('-start_date',)  # Urutkan berdasarkan tanggal mulai terbaru
