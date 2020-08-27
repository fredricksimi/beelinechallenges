from django.contrib import admin
from .models import Challenges, ChallengeAudience, Preapproved_challenge, ChallengeTag
from .forms import ChallengesModelForm

class ChallengesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title']

    # def get_form(self, request, obj=None, **kwargs):
    #     if obj.status == "Rolling":
    #         self.exclude('open_until')
    #     form = super(ChallengesAdmin, self).get_form(request, obj, **kwargs)
    #     return form
    # if status == "Rolling":
    #     exclude('open_until')

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'offered_by',
            'image', 'challenge_summary', 'description',
            'external_website_url', 'participate_link',
            'targeted_audience', 'tags', 'who_can_participate',
            'how_to_participate', 'prize', 'additional_information',
            'point_of_contact','status', 'date_posted',),
            'classes': ('predefined',)
        }),
        (None, {
            'fields': (('open_until'),),
            'classes': ('abcdefg')
        })
    )

    form = ChallengesModelForm
    class Media:
        js = ('/static/admin/js/base.js')

admin.site.site_header = "Research Administration"
admin.site.site_title = "Research"

admin.site.register(Challenges, ChallengesAdmin)
admin.site.register(ChallengeAudience)
admin.site.register(Preapproved_challenge)
admin.site.register(ChallengeTag)
