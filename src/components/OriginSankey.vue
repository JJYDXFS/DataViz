<template>
  <div id="my_sankey"></div>
</template>

<script>
import { defineComponent } from "vue";
import * as d3 from 'd3v4';
import { d3Sankey } from '../js/sankey.js'

export default defineComponent({
  data() {
    return {}
  },
  mounted(){
    var sankey=this;
    d3.csv("./data/sankey_67.csv", function(error, data) {
        sankey.drawSankey(data);
    });
  },

  methods:{
    /**
     * drawSankey - 绘制桑基图
     * https://bl.ocks.org/d3noob/06e72deea99e7b4859841f305f63ba85
     * @date 2021-06-03
     * @param data - 学历数据
     */
    drawSankey(data){
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
        var svg = d3.select("#my_sankey")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")");
        // units
        var units = "人";
        // 格式化变量
        var formatNumber = d3.format(",.0f"),    // zero decimal places
        format = function(d) { return formatNumber(d) + " " + units; },
        color = d3.scaleOrdinal(d3.schemeCategory10);
        // 定义桑基图
        var sankey = d3Sankey()
            .nodeWidth(36)
            .nodePadding(35)
            .size([width, height]);

        var path = sankey.link();

        // 初始化结点和边
        var graph = {"nodes" : [], "links" : []};
        // 从数据中导入结点和边
        data.forEach(function (d) {
            graph.nodes.push({ "name": d.source });
            graph.nodes.push({ "name": d.target });
            graph.links.push({ "source": d.source,
                            "target": d.target,
                            "value": +d.value });
        });
        // 只返回不重复的结点
        graph.nodes = d3.keys(d3.nest()
            .key(function (d) { return d.name; })
            .object(graph.nodes));

        // 遍历每条边，用结点的下标代替文字
        graph.links.forEach(function (d, i) {
            graph.links[i].source = graph.nodes.indexOf(graph.links[i].source);
            graph.links[i].target = graph.nodes.indexOf(graph.links[i].target);
        });

        // 遍历每个结点将 字符串数组 转为 对象数组
        graph.nodes.forEach(function (d, i) {
            graph.nodes[i] = { "name": d };
        });

        sankey
            .nodes(graph.nodes)
            .links(graph.links)
            .layout(32);

        // 移动结点的函数
        var dragmove = function (d) {
            d3.select(this)
            .attr("transform", 
                "translate(" 
                    + d.x + "," 
                    + (d.y = Math.max(0, Math.min(height - d.dy, d3.event.y))) + ")");
            sankey.relayout();
            link.attr("d", path);
        }

        // 添加边
        var link = svg.append("g").selectAll(".sankey-link")
            .data(graph.links)
            .enter().append("path")
            .attr("class", "sankey-link")
            .attr("d", path)
            .style("stroke-width", function(d) {
                // console.log(d);
                return Math.max(1, d.dy);
            })
            .sort(function(a, b) { return b.dy - a.dy; });

        // 添加边的 title
        link.append("title")
            .text(function(d) {
    		return d.source.name + " - " + 
                d.target.name + "\n" + format(d.value); });

        // 添加结点
        var node = svg.append("g").selectAll(".sankey-node")
            .data(graph.nodes)
            .enter().append("g")
            .attr("class", "sankey-node")
            .attr("transform", function(d) { 
                // console.log(d);
                return "translate(" + d.x + "," + d.y + ")"; })
            .call(d3.drag()
                .subject(function(d) {
                return d;
            })
            .on("start", function() {
                this.parentNode.appendChild(this);
            })
            .on("drag", dragmove));

        // 为结点添加矩形块
        node.append("rect")
            .attr("height", function(d) { return d.dy; })
            .attr("width", sankey.nodeWidth())
            .style("fill", function(d) { 
                return d.color = color(d.name.replace(/ .*/, "")); })
            .style("stroke", function(d) { 
                return d3.rgb(d.color).darker(2); })
            .append("title")
            .text(function(d) { 
                return d.name + "\n" + format(d.value); });

        // 为结点添加 title
        node.append("text")
            .attr("x", -6)
            .attr("y", function(d) { return d.dy / 2; })
            .attr("dy", ".35em")
            .attr("text-anchor", "end")
            .attr("transform", null)
            .text(function(d) { return d.name; })
            .filter(function(d) { return d.x < width / 2; })
            .attr("x", 6 + sankey.nodeWidth())
            .attr("text-anchor", "start");
    },
  }
})
</script>

<style>
.sankey-node rect {
  cursor: move;
  fill-opacity: .8;
  shape-rendering: crispEdges;
}

.sankey-node text {
  pointer-events: none;
  text-shadow: 0 1px 0 #fff;
}

.sankey-link {
  fill: none;
  stroke: #000;
  stroke-opacity: .2;
}

.sankey-link:hover {
  stroke-opacity: .5;
}
</style>
