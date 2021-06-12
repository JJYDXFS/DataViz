<template>
    <div id="my_chess">

    </div>
</template>

<script>
import { defineComponent } from "vue";
import * as d3 from 'd3';

export default defineComponent({
  data() {
    return {}
  },
  mounted(){
    this.drawChessChart();
  },

  methods:{
    drawChessChart() {
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
        var margin = {top: 10, right: 200, bottom: 60, left: 100},
        width = width*0.87 - margin.left - margin.right,
        height = height*0.9 - margin.top - margin.bottom;
        // 棋盘边长=min(width,height)
        let chess_length = Math.min(width,height)*1.2;
        // svg
        var svg = d3.select("#my_chess")
            .append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom);

        var bg = svg.append("image").attr("id","bg");
        bg.attr("x",150)
        .attr("y",0)
        .attr("width",chess_length)
        .attr("xlink:href","img/chess_bg.png");

        var c1=svg.append("circle")
        .attr("id","test")
        .attr("cx",202)
        .attr("cy",chess_length*0.445)
        .attr("stroke","#0066CC")
        .attr("stroke-width","3px")
        .attr("r",chess_length*0.125*0.35)
        .attr("fill", function(){
            var defs = svg.append("defs").attr("id","imgdefs");
            var testpattern = defs.append("pattern")
                .attr("id","testpattern")
                .attr("height",1)
                .attr("width",1);
            testpattern.append("image")
                .attr("x", -(25-30+5.8))
                .attr("y", -(25-30+5.8))
                .attr("width",60)
                .attr("xlink:href","img/顾宪成.jpg")
            
            return "url(#testpattern)";
        })



        // var bg = svg.append("rect").attr("id","bg")
        // var defs = svg.append("defs").attr("id","imgdefs");
        // var bgpattern = defs.append("pattern")
        //     .attr("id","bgpattern")
        //     .attr("height",height)
        //     .attr("width",width);
        // bgpattern.append("image")
        //     .attr("x", 200)
        //     .attr("y", 200)
        //     .attr("width",width)
        //     .attr("height",height)
        //     .attr("xlink:href","img/chess_bg.png")
        //     .attr("clip-path","url(#bg)");
    }
  }

})
</script>

<style>

</style>