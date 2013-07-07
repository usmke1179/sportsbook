# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BaseballLine'
        db.delete_table(u'book_baseballline')

        # Deleting model 'BasketballLine'
        db.delete_table(u'book_basketballline')

        # Deleting model 'FootballLine'
        db.delete_table(u'book_footballline')


    def backwards(self, orm):
        # Adding model 'BaseballLine'
        db.create_table(u'book_baseballline', (
            ('underodds', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('eventtime', self.gf('django.db.models.fields.DateTimeField')()),
            ('hodds', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('gamekey', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('periodnum', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('hpitcher', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('vml', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('hteam', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('vrot', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('hml', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('vodds', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('vteam', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('overodds', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('hrot', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('vspread', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1)),
            ('hspread', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1)),
            ('total', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1)),
            ('perioddesc', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('vpitcher', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'book', ['BaseballLine'])

        # Adding model 'BasketballLine'
        db.create_table(u'book_basketballline', (
            ('underodds', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('eventtime', self.gf('django.db.models.fields.DateTimeField')()),
            ('hodds', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('gamekey', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('lastupdated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('periodnum', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('vml', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('hteam', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('vrot', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('hml', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('vodds', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('vteam', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('overodds', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('hrot', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('vspread', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1)),
            ('hspread', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1)),
            ('total', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1)),
            ('perioddesc', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'book', ['BasketballLine'])

        # Adding model 'FootballLine'
        db.create_table(u'book_footballline', (
            ('underodds', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('eventtime', self.gf('django.db.models.fields.DateTimeField')()),
            ('hodds', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('gamekey', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('lastupdated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('periodnum', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('vml', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('hteam', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('vrot', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('hml', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('vodds', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('vteam', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('overodds', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('hrot', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('vspread', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1)),
            ('hspread', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1)),
            ('total', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1)),
            ('perioddesc', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'book', ['FootballLine'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'book.bet': {
            'Meta': {'object_name': 'Bet'},
            'bet_desc': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bet_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'eventtime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'risk': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'sport': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'to_win': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bets'", 'to': u"orm['auth.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['book']