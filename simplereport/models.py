from django.db import models, connection

class Report(models.Model):
    name=models.CharField(max_length=128)
    priority=models.IntegerField(default=0)
    query=models.TextField()
    
    class Meta:
        db_table='reports_report'
    
    def __unicode__(self):
        return self.name
    
    def run_link(self):
        return "<a href=\"%s\">run</a>" % self.get_absolute_url()
    run_link.allow_tags=True
    
    def get_absolute_url(self):
        return '/reports/detail/%s/' % self.id
    
    def get_results(self):
        cursor=connection.cursor()
        try:
            cursor.execute(self.query)
            return (cursor.description, cursor.fetchall())
        except Exception, e:
            return (['Error'], [['%s - %s' % (Exception, e)]])