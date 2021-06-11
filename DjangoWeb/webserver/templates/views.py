from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.shortcuts import render
from bs4 import BeautifulSoup

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./hello/templates"))

from pyecharts import options as opts
from pyecharts.charts import Gauge


def index(request):
    c = (
        Gauge()
            .add(series_name="业务指标", data_pair=[["", 55.5]])
            .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),
        )
    )

    # print(c.render_embed())
    soup = BeautifulSoup(c.render_embed(), 'html.parser')

    # 获取div
    div_li = soup.find_all('div')
    div_elm = str(div_li[0])
    div_style = div_li[0].get('style')
    div_elm = div_elm.replace(div_style, "width:500px; height:300px;")

    # 获取script
    div_script_list = soup.find_all('script')
    div_script_elm_list = []
    for div_script_elm in div_script_list:
        div_script_elm = str(div_script_elm)
        div_script_elm_list.append(div_script_elm)
    # 组织内容
    content = {
        'div_elm': div_elm,
        'div_script_elm_list': div_script_elm_list
    }
    return render(request, 'test.html', content)
