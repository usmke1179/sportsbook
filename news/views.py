from django.views.generic import ListView
from sportsbook.settings import base
from . import espyn


class NewsView(ListView):
    template_name = "news/index.html"
    context_object_name = "stories"
    paginate_by = 20

    def get_queryset(self):
        api_key = "hs6u5zg857xbyqdwp5dt6t5s"
        espn_object = espyn.ESPN(api_key)
        h = espn_object.headlines()
        queryset = []
        articles = h["headlines"]
        counter = 0
        for article in articles:
            d = {}
            d["headline"] = article["headline"]
            d["link"] = article["links"]["web"]["href"]
            d["description"] = article["description"]
            if len(article["images"]) > 0:
                d["imgurl"] = article["images"][0]["url"]
                if article["images"][0]["height"] == 324 and article["images"][0]["width"] == 576 and counter <= 5:
                    queryset.insert(counter, d)
                    counter += 1
                else:
                    queryset.append(d)
            else:
                d["imgurl"] = base.STATIC_URL + "images/espn.jpg"
                queryset.append(d)
        return queryset
