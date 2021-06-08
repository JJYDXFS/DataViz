<template>
    <div id="my_circle_packing"></div>
</template>
    
<script>
import { defineComponent } from "vue";
import * as d3 from 'd3';

export default defineComponent({
  data() {
    return {}
  },
  mounted(){
    var circlrPacking=this;
    d3.json("./data/pos_name.json").then(function(data) {
        circlrPacking.drawCirclePacking(data);
    });
  },

  methods:{
      /**
       * drawCirclePacking - 绘制CirclePacking树图
       * @date 2021-06-08
       * @param data - 树图数据
       * https://observablehq.com/@d3/zoomable-circle-packing
       */
      drawCirclePacking(data){
        
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
        var margin = {top: 10, right: 200, bottom: 10, left: 20},
        width = width*0.87 - margin.left - margin.right,
        height = height*0.9 - margin.top - margin.bottom;
        // 处理数据函数
        var pack = data => d3.pack()
            .size([width, height])
            .padding(3)
        (d3.hierarchy(data)
            .sum(d => d.value)
            .sort((a, b) => b.value - a.value));
        // color
        var color = d3.scaleLinear()
            .domain([0, 5])
            .range(["rgba(89, 181, 246, 0.4)", "rgba(149, 181, 246,0.4)"])
            .interpolate(d3.interpolateHcl);
        // 其他常量
        let focus = root;
        let view;
        // 缩放函数
        var zoomTo = function (v) {
            const k = width / v[2];

            view = v;

            label.attr("transform", d => `translate(${(d.x - v[0]) * k},${(d.y - v[1]) * k})`);
            node.attr("transform", d => `translate(${(d.x - v[0]) * k},${(d.y - v[1]) * k})`);
            node.attr("r", d => d.r * k);
        };

        var zoom = function (event,d){
            const focus0 = focus;

            focus = d;

            const transition = svg.transition()
                .duration(event.altKey ? 7500 : 750)
                .tween("zoom", d => {
                const i = d3.interpolateZoom(view, [focus.x, focus.y, focus.r * 3]);
                return t => zoomTo(i(t));
                });

            label
            .filter(function(d) { return d.parent === focus || this.style.display === "inline"; })
            .transition(transition)
                .style("fill-opacity", d => d.parent === focus ? 1 : 0)
                .on("start", function(d) { if (d.parent === focus) this.style.display = "inline"; })
                .on("end", function(d) { if (d.parent !== focus) this.style.display = "none"; });
        };
        // 处理数据
        var root = pack(data);

        // svg
        var svg = d3.select("#my_circle_packing")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform",
                "translate(" + (width*0.55) + "," + (height/2) + ")")
                .style("background", color(0))
                .style("cursor", "pointer")
                .on("click", (event) => zoom(event, root));
        
        // 绘制circle
        const node = svg.append("g")
            .selectAll("circle")
            .data(root.descendants().slice(1))
            .join("circle")
            .attr("fill", d => d.children ? color(d.depth) : "white")
            .attr("pointer-events", d => !d.children ? "none" : null)
            .on("mouseover", function() { d3.select(this).attr("stroke", "#000"); })
            .on("mouseout", function() { d3.select(this).attr("stroke", null); })
            .on("click", (event, d) => focus !== d && (zoom(event, d), event.stopPropagation()));
        
        // 绘制label
        const label = svg.append("g")
            .style("font", "10px sans-serif")
            .attr("pointer-events", "none")
            .attr("text-anchor", "middle")
            .selectAll("text")
            .data(root.descendants())
            .join("text")
            .style("fill-opacity", d => d.parent === root ? 1 : 0)
            .style("display", d => d.parent === root ? "inline" : "none")
            .style("font-size",20)
            .text(d => d.data.name);

        
        
        zoomTo([root.x, root.y, root.r * 3]);
    },
  }
})
</script>

<style>

</style>