from django.shortcuts import render
from django.db.models import Q
from itertools import chain
from django.views.generic import ListView


from singgasanaseni.models import *



"""def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            artist= Q(Nama__icontains=query) | Q(Panggilan__icontains=query)


            results= perupa.objects.filter(artist).distinct()


            context={'results': results,
                     'submitbutton': submitbutton,

                     }

            return render(request, 'search/search.html', context)

        else:
            return render(request, 'search/search.html')

    else:
        return render(request, 'search/search.html')"""

class SearchView(ListView):
        template_name = 'search/view.html'
        paginate_by = 20
        count = 0

        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context['count'] = self.count or 0
            context['query'] = self.request.GET.get('q')
            return context

        def get_queryset(self):
            request = self.request
            query = request.GET.get('q', None)

            if query is not None:
                karya_results = karya.object.search(query)
                perupa_results = perupa.object.search(query)
                berita_results = berita.object.search(query)

                # combine querysets
                queryset_chain = chain(
                    karya_results,
                    perupa_results,
                    berita_results
                )
                qs = sorted(queryset_chain,
                            key=lambda instance: instance.pk,
                            reverse=True)
                self.count = len(qs)  # since qs is actually a list
                return qs
            return karya.object.none()