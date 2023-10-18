# Generated by Django 4.2.3 on 2023-10-18 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='提供者'),
        ),
        migrations.AddField(
            model_name='position',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position_set', to='app.organization'),
        ),
        migrations.AddField(
            model_name='position',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position_set', to='app.naturalperson'),
        ),
        migrations.AddField(
            model_name='poolrecord',
            name='pool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pool', verbose_name='奖池'),
        ),
        migrations.AddField(
            model_name='poolrecord',
            name='prize',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.prize', verbose_name='奖品'),
        ),
        migrations.AddField(
            model_name='poolrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='poolitem',
            name='pool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pool', verbose_name='奖池'),
        ),
        migrations.AddField(
            model_name='poolitem',
            name='prize',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.prize', verbose_name='奖品'),
        ),
        migrations.AddField(
            model_name='participant',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.naturalperson'),
        ),
        migrations.AddField(
            model_name='organizationtype',
            name='incharge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='incharge', to='app.naturalperson'),
        ),
        migrations.AddField(
            model_name='organization',
            name='organization_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organization',
            name='otype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.organizationtype'),
        ),
        migrations.AddField(
            model_name='organization',
            name='tags',
            field=models.ManyToManyField(to='app.organizationtag'),
        ),
        migrations.AddField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recv_notice', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='relate_instance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relate_notifications', to='app.commentbase'),
        ),
        migrations.AddField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send_notice', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='naturalperson',
            name='person_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='naturalperson',
            name='unsubscribe_list',
            field=models.ManyToManyField(db_index=True, related_name='unsubscribers', to='app.organization'),
        ),
        migrations.AddField(
            model_name='modifyrecord',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modify_records', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.AddField(
            model_name='coursetime',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_set', to='app.course'),
        ),
        migrations.AddField(
            model_name='courserecord',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.course'),
        ),
        migrations.AddField(
            model_name='courserecord',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.naturalperson'),
        ),
        migrations.AddField(
            model_name='courseparticipant',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_set', to='app.course'),
        ),
        migrations.AddField(
            model_name='courseparticipant',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.naturalperson'),
        ),
        migrations.AddField(
            model_name='course',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.organization', verbose_name='开课组织'),
        ),
        migrations.AddField(
            model_name='commentphoto',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_photos', to='app.comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论者'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentbase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.commentbase'),
        ),
        migrations.AddField(
            model_name='academictextentry',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.naturalperson'),
        ),
        migrations.AddField(
            model_name='academictagentry',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.naturalperson'),
        ),
        migrations.AddField(
            model_name='academictagentry',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.academictag'),
        ),
        migrations.AddField(
            model_name='academicqaawards',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='participant',
            name='activity_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.activity'),
        ),
        migrations.AddField(
            model_name='modifyposition',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position_application', to='app.organization'),
        ),
        migrations.AddField(
            model_name='modifyposition',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position_application', to='app.naturalperson'),
        ),
        migrations.AddField(
            model_name='modifyorganization',
            name='otype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.organizationtype'),
        ),
        migrations.AddField(
            model_name='modifyorganization',
            name='pos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='questioner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send_chat_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='respondent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receive_chat_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activitysummary',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.activity'),
        ),
        migrations.AddField(
            model_name='activityphoto',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='app.activity'),
        ),
        migrations.AddField(
            model_name='activity',
            name='course_time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.coursetime', verbose_name='课程每周活动时间'),
        ),
        migrations.AddField(
            model_name='activity',
            name='examine_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.naturalperson', verbose_name='审核老师'),
        ),
        migrations.AddField(
            model_name='activity',
            name='organization_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.organization'),
        ),
        migrations.AddField(
            model_name='academicqa',
            name='chat',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.chat'),
        ),
    ]