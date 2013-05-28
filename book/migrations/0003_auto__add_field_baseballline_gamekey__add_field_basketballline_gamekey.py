# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BaseballLine.gamekey'
        db.add_column(u'book_baseballline', 'gamekey',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'BasketballLine.gamekey'
        db.add_column(u'book_basketballline', 'gamekey',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BaseballLine.gamekey'
        db.delete_column(u'book_baseballline', 'gamekey')

        # Deleting field 'BasketballLine.gamekey'
        db.delete_column(u'book_basketballline', 'gamekey')


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
        u'book.baseballline': {
            'Meta': {'object_name': 'BaseballLine'},
            'eventtime': ('django.db.models.fields.DateTimeField', [], {}),
            'gamekey': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hml': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hodds': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hpitcher': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'hrot': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hspread': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1'}),
            'hteam': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastupdated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'overodds': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'perioddesc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'periodnum': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1'}),
            'underodds': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'vml': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'vodds': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'vpitcher': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'vrot': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'vspread': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1'}),
            'vteam': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'book.basketballline': {
            'Meta': {'object_name': 'BasketballLine'},
            'eventtime': ('django.db.models.fields.DateTimeField', [], {}),
            'gamekey': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hml': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hodds': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hrot': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hspread': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1'}),
            'hteam': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastupdated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'overodds': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'perioddesc': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'periodnum': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1'}),
            'underodds': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'vml': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'vodds': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'vrot': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'vspread': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1'}),
            'vteam': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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