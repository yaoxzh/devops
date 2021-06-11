import pyecharts.options as opts
from pyecharts.charts import Gauge
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
def spwan_img():
    a = (
    Gauge()
    .add("", [("cpu使用率", 66.6)])
    .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-基本示例"))
)
    return a


make_snapshot(snapshot, spwan_img().render(), "gauge.png")
