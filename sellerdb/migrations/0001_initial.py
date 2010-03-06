
from south.db import db
from django.db import models
from cdepot.sellerdb.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Seller'
        db.create_table('sellerdb_seller', (
            ('id', orm['sellerdb.Seller:id']),
            ('first_name', orm['sellerdb.Seller:first_name']),
            ('middle_name', orm['sellerdb.Seller:middle_name']),
            ('last_name', orm['sellerdb.Seller:last_name']),
            ('address', orm['sellerdb.Seller:address']),
            ('license_number', orm['sellerdb.Seller:license_number']),
            ('license_state', orm['sellerdb.Seller:license_state']),
            ('birthday', orm['sellerdb.Seller:birthday']),
            ('license_expires', orm['sellerdb.Seller:license_expires']),
            ('first_created', orm['sellerdb.Seller:first_created']),
        ))
        db.send_create_signal('sellerdb', ['Seller'])
        
        # Adding model 'DatesVisited'
        db.create_table('sellerdb_datesvisited', (
            ('id', orm['sellerdb.DatesVisited:id']),
            ('date_visited', orm['sellerdb.DatesVisited:date_visited']),
        ))
        db.send_create_signal('sellerdb', ['DatesVisited'])
        
        # Adding ManyToManyField 'DatesVisited.sellers'
        db.create_table('sellerdb_datesvisited_sellers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('datesvisited', models.ForeignKey(orm.DatesVisited, null=False)),
            ('seller', models.ForeignKey(orm.Seller, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Seller'
        db.delete_table('sellerdb_seller')
        
        # Deleting model 'DatesVisited'
        db.delete_table('sellerdb_datesvisited')
        
        # Dropping ManyToManyField 'DatesVisited.sellers'
        db.delete_table('sellerdb_datesvisited_sellers')
        
    
    
    models = {
        'sellerdb.datesvisited': {
            'date_visited': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'unique': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sellers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sellerdb.Seller']"})
        },
        'sellerdb.seller': {
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'first_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'license_expires': ('django.db.models.fields.DateField', [], {}),
            'license_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'license_state': ('django.db.models.fields.IntegerField', [], {'default': '23', 'max_length': '30'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }
    
    complete_apps = ['sellerdb']
