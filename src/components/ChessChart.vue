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
    var chess=this;
    d3.json("./data/chess.json").then(function(data) {
        chess.drawChessChart(data);
    });
  },

  methods:{
    drawChessChart(data) {
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
        // 交互事件
        // 交互事件
        var mouseover = function(event,d) {
            // scatter_tooltip.style("opacity", 1);
            console.log(d);
            d3.select(this).attr("stroke-width","4px");
        }
    
        var mousemove = function(event,d) {
            let point_this = this;
            let point_cx = d3.select(point_this).attr("cx");

            scatter_tooltip
            .html(d.name+" "+"<br/>"+d.begin_title+"<br/>"+"在任时长："+d.scale+"年")
            .style("left", function(d){
                    
                if(point_cx < (width-120)){
                    return (d3.pointer(event,point_this)[0]+30) + "px"
                }
                else {
                    return (d3.pointer(event,point_this)[0]-160) + "px"
                }
                    
            }) // 90是最佳实践
            .style("top", (d3.pointer(event,this)[1]) + "px")
        }
            
        var mouseleave = function(event,d) {
            d3.select(this).attr("stroke-width","2px");
        }
        // 棋盘背景
        var bg = svg.append("image").attr("id","bg");
        bg.attr("x",150)
        .attr("y",0)
        .attr("width",chess_length)
        .attr("xlink:href","img/chess_bg.png");
        // 绘制棋子
        var img_w=50;
        var radius=chess_length*0.125*0.35;
        var left_boundry = 202;
        var top_boundry = 40;
        var dxy=chess_length*0.095;

        var chessman=svg.selectAll("chessman")
            .data(data)
            .enter()
            .append("circle")
                .attr("cx",function(d){
                    if(d.pos_x<5){
                        return left_boundry+d.pos_x*dxy;
                    }
                    return left_boundry+d.pos_x*(dxy*0.99);
                })
                .attr("cy",d=>(top_boundry+d.pos_y*dxy))
                .attr("stroke",function(d){
                    if(d.isPM == 1){
                        return "#FFFF00";
                    }
                    return "#0066CC";
                })
                .attr("stroke-width","2px")
                .attr("r",radius)
                .attr("fill", function(d,i){
                    var defs = svg.append("defs").attr("id","imgdefs");
                    var testpattern = defs.append("pattern")
                        .attr("id","chesspattern"+i)
                        .attr("height",1)
                        .attr("width",1);
                    testpattern.append("image")
                        .attr("x", -(img_w/2-radius+5.8))
                        .attr("y", -(img_w/2-radius+5.8))
                        .attr("width",60)
                        .attr("xlink:href",`img/${d.name}.jpg`)
                    
                    return "url(#chesspattern"+i+")";
                });

        chessman.on("mouseover", mouseover)
            .on("mouseleave", mouseleave);

            
    }
  }

})
</script>

<style>

</style>