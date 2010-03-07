from django.db import models
from django.contrib import admin
import datetime

# Create your models here.
class Seller(models.Model):

    STATES = (
        (1 ,"Alabama"),
        (2 ,"Alaska"),
        (3 ,"American Samoa"),
        (4 ,"Arizona"),
        (5 ,"Arkansas"),
        (6 ,"California"),
        (7 ,"Colorado"),
        (8 ,"Connecticut"),
        (9 ,"Delaware"),
        (10 ,"District of Columbia"),
        (11 ,"Florida"),
        (12 ,"Georgia"),
        (13 ,"Guam"),
        (14 ,"Hawaii"),
        (15 ,"Idaho"),
        (16 ,"Illinois"),
        (17 ,"Indiana"),
        (18 ,"Iowa"),
        (19 ,"Kansas"),
        (20 ,"Kentucky"),
        (21 ,"Louisiana"),
        (22 ,"Maine"),
        (23 ,"Maryland"),
        (24 ,"Massachusetts"),
        (25 ,"Michigan"),
        (26 ,"Minnesota"),
        (27 ,"Mississippi"),
        (28 ,"Missouri"),
        (29 ,"Montana"),
        (30 ,"Nebraska"),
        (31 ,"Nevada"),
        (32 ,"New Hampshire"),
        (33 ,"New Jersey"),
        (34 ,"New Mexico"),
        (35 ,"New York"),
        (36 ,"North Carolina"),
        (37 ,"North Dakota"),
        (38 ,"Northern Marianas Islands"),
        (39 ,"Ohio"),
        (40 ,"Oklahoma"),
        (41 ,"Oregon"),
        (42 ,"Pennsylvania"),
        (43 ,"Puerto Rico"),
        (44 ,"Rhode Island"),
        (45 ,"South Carolina"),
        (46 ,"South Dakota"),
        (47 ,"Tennessee"),
        (48 ,"Texas"),
        (49 ,"Utah"),
        (50 ,"Vermont"),
        (51 ,"Virginia"),
        (52 ,"Virgin Islands"),
        (53 ,"Washington"),
        (54 ,"West Virginia"),
        (55 ,"Wisconsin"),
        (56 ,"Wyoming"),
    )    
    
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    
    address = models.CharField(max_length=200)
    
    license_number = models.CharField(max_length=30, unique=True)
    license_state = models.IntegerField(max_length=30, choices=STATES, default=23)

    birthday = models.DateField(blank=False, help_text="Enter in YYYY-MM-DD format")
    
    license_expires = models.DateField(help_text="Enter in YYYY-MM-DD format")
    
    first_created = models.DateField(auto_now_add=True)
    
    dates_visited = models.ManyToManyField("Date", through="DatesVisited")
    
    class Meta: 
        ordering = ['last_name']
    
    def __unicode__(self):
        return "%s, %s %s" % (self.last_name, self.first_name, self.middle_name)


class Date(models.Model):
    date_visited = models.DateField()
    
    class Meta: 
        verbose_name = "Date(s) Visited"
        verbose_name_plural = "Dates Visited"
    
    def __unicode__(self):
        return self.date_visited.strftime("%A %d. %B %Y")
    
    
class DateInline(admin.TabularInline):
    model = Date
#    prepopulated_fields = {'date_visited' : ( datetime.datetime.today, )} 

    
class DatesVisited(models.Model):
    seller = models.ForeignKey(Seller)
    date = models.ForeignKey(Date)
    
class DatesVisitedInline(admin.TabularInline):
    model = DatesVisited
    extra = 1
    verbose_name = "Dates Visited"
    verbose_name_plural = "Dates Visited"
    


    
class SellerAdmin(admin.ModelAdmin):
#    date_hierarchy = 'first_created'
    list_display = ('__unicode__', 'last_name', 'first_name', 'license_state', 'license_number', 'birthday')
    list_display_links = ('last_name', 'first_name', 'license_state', 'license_number')
    list_filter = ('license_state',)
    list_per_page = 100
    search_fields = ('first_name', 'last_name', 'license_number', 'birthday')
#    fieldsets = [
#        ('License', {'fields': ['license_number', 'license_state']}),        
#        ('Person', {'fields': ['first_name', 'middle_name', 'last_name', 'address']}),
#        ('Dates', {'fields': ['birthday', 'license_expires']}),
#    ]
    readonly_fields = ('last_name', 'first_name', 'license_state')
    inlines = (DatesVisitedInline,)

    
    
    
admin.site.disable_action('delete_selected')       
#admin.site.register(DatesVisited, DatesVisitedAdmin)    
admin.site.register(Seller, SellerAdmin)