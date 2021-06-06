<template>
    <div id="my_scatter"></div>
</template>

<script>
import { defineComponent } from "vue";
import * as d3 from "d3";

export default defineComponent({
    data(){
        return {}
    },
    mounted(){
        var scatter=this;
        d3.csv("./scatter_data.csv").then(function(data) {
            scatter.drawScatter(data);
        });
    },

    methods:{
        /**
        * drawScatter - 绘制散点图
         * @date 2021-06-01
         * @param data - 任职表数据
         */
        drawScatter(data){
            // 有关svg的数据
            /* 常量
            ---------------------------------------------------------------------------------------------------*/
            var width = window.innerWidth
            || document.documentElement.clientWidth
            || document.body.clientWidth;

            var height = window.innerHeight
            || document.documentElement.clientHeight
            || document.body.clientHeight;
            // 边距
            var margin = {top: 10, right: 200, bottom: 60, left: 20},
            width = width*0.87 - margin.left - margin.right,
            height = height*0.9 - margin.top - margin.bottom;
            // svg
            var svg = d3.select("#my_scatter")
                .append("svg")
                    .attr("width", width + margin.left + margin.right)
                    .attr("height", height + margin.top + margin.bottom)
                .append("g")
                    .attr("transform",
                        "translate(" + margin.left + "," + margin.top + ")");
            // 颜色映射字典
            var color_domain=["YL","YLRXZT",
                "ZT","ZTJT","JT","TS","TSCH","CH","CHHZ",
                "HZ","HZZD","ZD","ZDJJ","JJ","LQ","JJLQ","LQWL",
                "WL","WLTC","TC","TCTQ","TQ","TQCZ","CZ"];
            // 年号和代号映射（可以在数据库中修改）
            var title_map={"永乐":"YL",
                "永乐 仁宣 正统":"YLRXZT","正统":"ZT","正统 景泰":"ZTJT",
                "景泰":"JT","天顺":"TS","天顺 成化":"TSCH","成化":"CH",
                "成化 弘治":"CHHZ","弘治":"HZ","弘治 正德":"HZZD","正德":"ZD",
                "正德 嘉靖":"ZDJJ","嘉靖":"JJ","隆庆":"LQ","嘉靖 隆庆":"JJLQ",
                "隆庆 万历":"LQWL","万历":"WL","万历 泰昌":"WLTC","泰昌":"TC",
                "泰昌 天启":"TCTQ","天启":"TQ","天启 崇祯":"TQCZ","崇祯":"CZ"}
            // 年号坐标
            var time_title=[
                //{"time":"1368-01-01","title":"洪武"},
                //{"time":"1398-01-01","title":"建文"},
                {"time":"1402-08-01","title":"永乐"},
                //{"time":"1424-01-01","title":"洪熙"},
                {"time":"1425-01-01","title":"宣德"},
                {"time":"1435-01-01","title":"正统"},
                {"time":"1449-01-01","title":"景泰"},
                {"time":"1457-01-01","title":"天顺"},
                {"time":"1464-01-01","title":"成化"},
                {"time":"1487-01-01","title":"弘治"},
                {"time":"1505-01-01","title":"正德"},
                {"time":"1521-01-01","title":"嘉靖"},
                {"time":"1566-01-01","title":"隆庆"},
                {"time":"1572-01-01","title":"万历"},
                {"time":"1620-01-01","title":"(泰昌)天启"},
                {"time":"1627-01-01","title":"崇祯"},
                {"time":"1644-03-01","title":"明亡"}
            ];
            // x轴刻度
            var xAxis_tick=[];
            // 需要提前定义的全局变量&处理函数
            var myDots;
            // 坐标轴
            var x = d3.scaleTime().range([0, width]);
            var y = d3.scaleLinear().range([height, 0]);
            /* 函数 
            ---------------------------------------------------------------------------------------------------*/
            // 格式化时间
            var parseTime = d3.timeParse("%Y-%m-%d");
            var FormatYear = d3.timeFormat("%Y");
            // 将年号坐标转为时间坐标
            time_title.forEach(function(d){ 
                d.time=parseTime(d.time);
                xAxis_tick.push(d.time);
            })
            // 颜色函数
            var circle_color=d3.scaleOrdinal(d3.schemeCategory10);
            // 绘制x轴网格线
            var make_x_gridlines=function() {
                return d3.axisBottom(x)
                .ticks(24);
            };
            // 绘制y轴网格线
            var make_y_gridlines=function() {
                return d3.axisLeft(y)
                .ticks(10);
            };

            // 格式化数据
            data.forEach(function(d) {
                d.begin = parseTime(d.begin);
            });
            // 把字符串类型的数字转为数字
            data.forEach(function(d) {
                d.scale = parseFloat(d.scale);
            });
            // axis+grid
            x.domain(d3.extent(data, function(d) { return d.begin; }));
            y.domain([0, d3.max(data, function(d) { return d.scale; })]);

            // Add the X Axis
            svg.append("g")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x)
                        .tickValues(xAxis_tick)
                        .tickFormat(FormatYear)
                        .tickSize(8))
                .selectAll("text")	
                    .style("text-anchor", "end")
                    .style("font-size","12px")
                    .attr("dx", "1em")
                    .attr("dy", "1em")
                    .attr("transform", "rotate(0)");

            // Add the Y Axis
            svg.append("g")
                .call(d3.axisLeft(y));

            // Add the X gridlines
            svg.append("g")			
                .attr("class", "grid")
                .call(make_x_gridlines()
                    .tickSize(height)
                    .tickFormat("")
                )

            // add the Y gridlines
            svg.append("g")			
                .attr("class", "grid")
                .call(make_y_gridlines()
                    .tickSize(-width)
                    .tickFormat("")
                )

            // add axis title
            // Y axis label:
            svg.append("text")
                .attr("text-anchor", "end")
                .attr("transform", "rotate(-90)")
                .attr("y", -margin.left+40)
                .attr("x", -margin.top+10)
                .text("在任时长（年）")

            // tooltip
            var scatter_tooltip = d3.select("#my_scatter")
                .append("div")
                .style("opacity", 0)
                .attr("class", "scatter_tooltip")
                .style("background-color", "white")
                .style("border", "solid")
                .style("border-width", "1px")
                .style("border-radius", "5px")
                .style("padding", "10px")
            
            var mouseover = function(event,d) {
                scatter_tooltip.style("opacity", 1)}
    
            var mousemove = function(event,d) {
                scatter_tooltip
                .html(d.name+" "+"<br/>"+d.begin_title+"<br/>"+"在任时长："+d.scale+"年")
                .style("left", (d3.pointer(event,this)[0]+30) + "px") // 90是最佳实践
                .style("top", (d3.pointer(event,this)[1]) + "px")
            }
            
            var mouseleave = function(event,d) {
                scatter_tooltip
                .transition()
                .duration(200)
                .style("opacity", 0)
            }
            // dots
            myDots=svg.append('g')
                .selectAll("dot")
                .data(data)
                .enter()
                .append("circle")
                .attr("cx", 0)
                .attr("cy", d=>y(d.scale))
                .attr("r", 0)
                .style("fill", function(d){
                    return circle_color(title_map[d.em]);
                })
                .style("opacity", 0.5)
                .style("stroke", "white")
                .on("mouseover", mouseover )
                .on("mousemove", mousemove )
                .on("mouseleave", mouseleave );
            // 加动画
            svg.selectAll("circle")
                .transition()
                .delay(function(d,i){return(i*5)})
                .duration(2000)
                .attr("cx", d=>x(d.begin))
                .attr("r",9);
                //.attr("cy", d=>y(d.scale))
        },
    }
},
)

</script>

<style>

div.scatter_tooltip {	
    position: absolute;			
    text-align: center;			
    width: 150px;					
    height: 60px;					
    padding: 2px;				
    font: 12px sans-serif;
    line-height: 20px;	
    border: 0px;	
    border-radius: 8px;			
    pointer-events: none;			
}

.grid line {
    stroke: lightgrey;
    stroke-opacity: 0.5;
    shape-rendering: crispEdges;
}

.grid path {
  stroke-width: 0;
}
</style>