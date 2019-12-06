# Generated by Django 2.2.7 on 2019-11-21 21:29

import colorfield.fields
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='AffectedGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affected_group_name', models.CharField(max_length=100)),
                ('affected_group_name_en', models.CharField(max_length=100, null=True)),
                ('affected_group_name_ru', models.CharField(max_length=100, null=True)),
                ('affected_group_name_uk', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Affected Group',
                'verbose_name_plural': 'Affected Groups',
                'db_table': 'affected_groups',
            },
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_referal', models.DateField(verbose_name='Date of Incident')),
                ('informant', models.TextField(blank=True, null=True)),
                ('conflict_related', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('description', models.TextField(blank=True, null=True)),
                ('context', models.TextField(blank=True, null=True)),
                ('source_info', models.CharField(blank=True, max_length=255, null=True)),
                ('date_update', models.DateField(blank=True, null=True)),
                ('additional_info_link', models.CharField(blank=True, max_length=255, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('population', models.BigIntegerField(blank=True, null=True, verbose_name='Baseline population')),
                ('population_males', models.BigIntegerField(blank=True, null=True)),
                ('population_females', models.BigIntegerField(blank=True, null=True)),
                ('population_children', models.BigIntegerField(blank=True, null=True)),
                ('population_adult', models.BigIntegerField(blank=True, null=True)),
                ('population_elderly', models.BigIntegerField(blank=True, null=True)),
                ('no_affected', models.IntegerField(verbose_name='Number of affected (ind.)')),
                ('no_affected_males', models.BigIntegerField(blank=True, null=True)),
                ('no_affected_females', models.BigIntegerField(blank=True, null=True)),
                ('no_affected_children', models.BigIntegerField(blank=True, null=True)),
                ('no_affected_adult', models.BigIntegerField(blank=True, null=True)),
                ('no_affected_elderly', models.BigIntegerField(blank=True, null=True)),
                ('no_beneficiaries', models.IntegerField(blank=True, null=True, verbose_name='Number of beneficiaries')),
                ('no_beneficiaries_males', models.BigIntegerField(blank=True, null=True)),
                ('no_beneficiaries_females', models.BigIntegerField(blank=True, null=True)),
                ('no_beneficiaries_children', models.BigIntegerField(blank=True, null=True)),
                ('no_beneficiaries_adult', models.BigIntegerField(blank=True, null=True)),
                ('no_beneficiaries_elderly', models.BigIntegerField(blank=True, null=True)),
                ('affected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='affected_id', to='AlertsMap.AffectedGroup', verbose_name='Affected group')),
            ],
            options={
                'db_table': 'alerts',
            },
        ),
        migrations.CreateModel(
            name='AlertType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_type', models.CharField(blank=True, max_length=50, null=True)),
                ('alert_type_en', models.CharField(blank=True, max_length=50, null=True)),
                ('alert_type_ru', models.CharField(blank=True, max_length=50, null=True)),
                ('alert_type_uk', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Alert Type',
                'verbose_name_plural': 'Alert Types',
                'db_table': 'alert_types',
            },
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster_name', models.CharField(max_length=200)),
                ('cluster_name_en', models.CharField(max_length=200, null=True)),
                ('cluster_name_ru', models.CharField(max_length=200, null=True)),
                ('cluster_name_uk', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Cluster',
                'verbose_name_plural': 'Clusters',
                'db_table': 'clusters',
            },
        ),
        migrations.CreateModel(
            name='ConfirmationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation_status', models.CharField(max_length=30)),
                ('confirmation_status_en', models.CharField(max_length=30, null=True)),
                ('confirmation_status_ru', models.CharField(max_length=30, null=True)),
                ('confirmation_status_uk', models.CharField(max_length=30, null=True)),
            ],
            options={
                'db_table': 'confirmation_status',
            },
        ),
        migrations.CreateModel(
            name='CoordinationHub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Coordination hub',
                'verbose_name_plural': 'Coordination hubs',
                'db_table': 'coordination_hubs',
            },
        ),
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emails',
                'db_table': 'emails',
            },
        ),
        migrations.CreateModel(
            name='GCA_NGCA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_area', models.CharField(max_length=20)),
                ('type_of_area_en', models.CharField(max_length=20, null=True)),
                ('type_of_area_ru', models.CharField(max_length=20, null=True)),
                ('type_of_area_uk', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'gca_ngca',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=120, null=True)),
                ('item_name_en', models.CharField(blank=True, max_length=120, null=True)),
                ('item_name_ru', models.CharField(blank=True, max_length=120, null=True)),
                ('item_name_uk', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='ItemGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_group_name', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'db_table': 'item_groups',
            },
        ),
        migrations.CreateModel(
            name='MapConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zoom', models.IntegerField()),
                ('min_zoom', models.IntegerField()),
                ('max_zoom', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NeedType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('need_type', models.CharField(max_length=50)),
                ('need_type_en', models.CharField(max_length=50, null=True)),
                ('need_type_ru', models.CharField(max_length=50, null=True)),
                ('need_type_uk', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Need Type',
                'verbose_name_plural': 'Need Types',
                'db_table': 'need_types',
            },
        ),
        migrations.CreateModel(
            name='Oblast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcode', models.CharField(blank=True, max_length=10, null=True)),
                ('oblast_name', models.CharField(max_length=100)),
                ('oblast_name_en', models.CharField(max_length=100, null=True)),
                ('oblast_name_ru', models.CharField(max_length=100, null=True)),
                ('oblast_name_uk', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Oblast',
                'verbose_name_plural': 'Oblasts',
                'db_table': 'oblasts',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=80, verbose_name='Organization Name')),
                ('organization_name_en', models.CharField(max_length=80, null=True, verbose_name='Organization Name')),
                ('organization_name_ru', models.CharField(max_length=80, null=True, verbose_name='Organization Name')),
                ('organization_name_uk', models.CharField(max_length=80, null=True, verbose_name='Organization Name')),
                ('organization_acronym', models.CharField(max_length=30, null=True)),
                ('organization_acronym_en', models.CharField(max_length=30, null=True)),
                ('organization_acronym_ru', models.CharField(max_length=30, null=True)),
                ('organization_acronym_uk', models.CharField(max_length=30, null=True)),
            ],
            options={
                'db_table': 'organizations',
                'ordering': ['organization_name'],
            },
        ),
        migrations.CreateModel(
            name='OrganizationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=80, null=True)),
                ('type_en', models.CharField(max_length=80, null=True)),
                ('type_ru', models.CharField(max_length=80, null=True)),
                ('type_uk', models.CharField(max_length=80, null=True)),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
                'db_table': 'organization_types',
            },
        ),
        migrations.CreateModel(
            name='Raion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcode', models.CharField(blank=True, max_length=10, null=True)),
                ('raion_name', models.CharField(max_length=100)),
                ('raion_name_en', models.CharField(max_length=100, null=True)),
                ('raion_name_ru', models.CharField(max_length=100, null=True)),
                ('raion_name_uk', models.CharField(max_length=100, null=True)),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
                ('oblast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.Oblast')),
            ],
            options={
                'verbose_name': 'Raion',
                'verbose_name_plural': 'Raions',
                'db_table': 'raions',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('status_en', models.CharField(max_length=50, null=True)),
                ('status_ru', models.CharField(max_length=50, null=True)),
                ('status_uk', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Statuses',
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(blank=True, max_length=30, null=True)),
                ('unit_name_en', models.CharField(blank=True, max_length=30, null=True)),
                ('unit_name_ru', models.CharField(blank=True, max_length=30, null=True)),
                ('unit_name_uk', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'item_units',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('organization', models.CharField(blank=True, max_length=80)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcode', models.CharField(blank=True, max_length=10, null=True)),
                ('pcode_new', models.CharField(blank=True, max_length=10, null=True)),
                ('settlement_name_old', models.CharField(blank=True, max_length=120, null=True)),
                ('settlement_name', models.CharField(max_length=120)),
                ('settlement_name_en', models.CharField(max_length=120, null=True)),
                ('settlement_name_ru', models.CharField(max_length=120, null=True)),
                ('settlement_name_uk', models.CharField(max_length=120, null=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.GCA_NGCA')),
                ('hub', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.CoordinationHub')),
                ('raion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.Raion')),
            ],
            options={
                'verbose_name': 'Settlement',
                'verbose_name_plural': 'Settlements',
                'db_table': 'settlements',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_details', models.CharField(blank=True, max_length=120, null=True)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField(blank=True, null=True)),
                ('uncovered_needs', models.CharField(blank=True, max_length=255, null=True)),
                ('action', models.CharField(blank=True, max_length=255, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='AlertsMap.Alert')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.Item')),
                ('response_partners', models.ManyToManyField(related_name='response_partners_id', to='AlertsMap.Organization')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.Unit')),
            ],
            options={
                'db_table': 'responses',
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='organization_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.OrganizationType'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.ItemGroup'),
        ),
        migrations.CreateModel(
            name='ClusterEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_list', models.ManyToManyField(related_name='cc_emails', to='AlertsMap.Emails')),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.Cluster')),
                ('coordination_hub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.CoordinationHub')),
                ('to_list', models.ManyToManyField(related_name='to_emails', to='AlertsMap.Emails')),
            ],
            options={
                'db_table': 'cluster_emails',
            },
        ),
        migrations.CreateModel(
            name='AlertItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_details', models.CharField(blank=True, max_length=120, null=True)),
                ('quantity', models.IntegerField()),
                ('alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='AlertsMap.Alert')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.Item')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.Unit')),
            ],
            options={
                'db_table': 'alert_items',
            },
        ),
        migrations.AddField(
            model_name='alert',
            name='alert_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.AlertType'),
        ),
        migrations.AddField(
            model_name='alert',
            name='clusters',
            field=models.ManyToManyField(related_name='clusters_id', to='AlertsMap.Cluster'),
        ),
        migrations.AddField(
            model_name='alert',
            name='confirmation_status',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.ConfirmationStatus'),
        ),
        migrations.AddField(
            model_name='alert',
            name='gca_ngca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.GCA_NGCA', verbose_name='GCA/NGCA'),
        ),
        migrations.AddField(
            model_name='alert',
            name='need_types',
            field=models.ManyToManyField(related_name='needs', to='AlertsMap.NeedType'),
        ),
        migrations.AddField(
            model_name='alert',
            name='oblast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.Oblast'),
        ),
        migrations.AddField(
            model_name='alert',
            name='raion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.Raion'),
        ),
        migrations.AddField(
            model_name='alert',
            name='referral_agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referral_agency_id', to='AlertsMap.Organization'),
        ),
        migrations.AddField(
            model_name='alert',
            name='settlement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.Settlement'),
        ),
        migrations.AddField(
            model_name='alert',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlertsMap.Status'),
        ),
    ]
