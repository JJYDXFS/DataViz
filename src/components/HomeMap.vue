<template>
    <div id="my_map"></div>
</template>

<script>
import { defineComponent } from "vue";
import * as d3 from 'd3';

export default defineComponent({
    data() {
        return {

        }
    },
    mounted(){
        var homeMap=this;
        d3.json("./data/map_data.json").then(function(map_res){
                d3.json("./map/China.geojson").then(function(res) {
                    // console.log(map_res);
                    homeMap.drawMap(res,map_res);
                });
        })
    },
    methods:{
        /**
         * drawMap - 绘制籍贯地图
         * @date 2021-06-02
         * @param res - 籍贯信息数据
         * @param map_data - 地图geojson数据
         */
        drawMap(res,map_data){
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
            var margin = {top: 10, right: 300, bottom: 60, left: 20},
            width = width*0.87 - margin.left - margin.right,
            height = height*0.9 - margin.top - margin.bottom;
            // svg
            var map_group = d3.select("#my_map")
                .append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                    .attr("transform",
                        "translate(" + margin.left + "," + margin.top + ")")
                    .attr("id","map");

            var root = null ;
            root = res;

            var title_list = ["永乐","仁宣","正统","景泰","天顺","成化","弘治","正德","嘉靖","万历","泰昌","天启","崇祯"];
            var dynamic_map_data =[
                {"江西":3,"浙江":1,"江苏":0,"河北":0,"山东":0,"福建":1,"四川":0,"河南":0,"山西":0,"北京":0,"湖北":0,"陕西":0,"广西":0,"湖南":0,"安徽":0,"广东":0,"云南":0,"上海":0},
                {"江西":3,"浙江":1,"江苏":0,"河北":0,"山东":0,"福建":1,"四川":0,"河南":0,"山西":0,"北京":0,"湖北":0,"陕西":0,"广西":0,"湖南":0,"安徽":0,"广东":0,"云南":0,"上海":0},
                {"江西":3,"浙江":1,"江苏":0,"河北":1,"山东":0,"福建":1,"四川":0,"河南":0,"山西":0,"北京":0,"湖北":1,"陕西":0,"广西":0,"湖南":0,"安徽":0,"广东":0,"云南":0,"上海":0},
                {"江西":4,"浙江":1,"江苏":0,"河北":1,"山东":0,"福建":1,"四川":0,"河南":0,"山西":0,"北京":0,"湖北":1,"陕西":0,"广西":0,"湖南":0,"安徽":0,"广东":0,"云南":0,"上海":0},
                {"江西":4,"浙江":1,"江苏":2,"河北":1,"山东":1,"福建":1,"四川":0,"河南":1,"山西":0,"北京":0,"湖北":1,"陕西":0,"广西":0,"湖南":0,"安徽":0,"广东":0,"云南":0,"上海":0},
                {"江西":6,"浙江":2,"江苏":2,"河北":1,"山东":1,"福建":1,"四川":1,"河南":1,"山西":0,"北京":0,"湖北":1,"陕西":0,"广西":0,"湖南":0,"安徽":0,"广东":0,"云南":0,"上海":0},
                {"江西":6,"浙江":2,"江苏":3,"河北":2,"山东":1,"福建":1,"四川":1,"河南":2,"山西":0,"北京":0,"湖北":1,"陕西":0,"广西":0,"湖南":0,"安徽":0,"广东":0,"云南":0,"上海":0},
                {"江西":6,"浙江":2,"江苏":3,"河北":2,"山东":1,"福建":1,"四川":2,"河南":2,"山西":0,"北京":0,"湖北":1,"陕西":0,"广西":0,"湖南":1,"安徽":0,"广东":1,"云南":0,"上海":0},
                {"江西":9,"浙江":3,"江苏":4,"河北":3,"山东":2,"福建":1,"四川":2,"河南":2,"山西":0,"北京":1,"湖北":1,"陕西":0,"广西":1,"湖南":1,"安徽":0,"广东":1,"云南":1,"上海":1},
                {"江西":9,"浙江":3,"江苏":5,"河北":3,"山东":2,"福建":1,"四川":2,"河南":3,"山西":0,"北京":1,"湖北":2,"陕西":0,"广西":1,"湖南":1,"安徽":0,"广东":1,"云南":1,"上海":1},
                {"江西":9,"浙江":6,"江苏":7,"河北":3,"山东":2,"福建":3,"四川":2,"河南":3,"山西":2,"北京":2,"湖北":2,"陕西":0,"广西":1,"湖南":1,"安徽":0,"广东":1,"云南":1,"上海":1},
                {"江西":9,"浙江":6,"江苏":7,"河北":3,"山东":2,"福建":3,"四川":2,"河南":3,"山西":2,"北京":2,"湖北":2,"陕西":0,"广西":1,"湖南":1,"安徽":0,"广东":1,"云南":1,"上海":1},
                {"江西":10,"浙江":7,"江苏":8,"河北":4,"山东":2,"福建":3,"四川":2,"河南":3,"山西":3,"北京":2,"湖北":2,"陕西":0,"广西":1,"湖南":1,"安徽":0,"广东":1,"云南":1,"上海":1},
                {"江西":10,"浙江":10,"江苏":9,"河北":7,"山东":5,"福建":4,"四川":4,"河南":3,"山西":3,"北京":3,"湖北":2,"陕西":1,"广西":1,"湖南":1,"安徽":1,"广东":1,"云南":1,"上海":1}
            ];
            var final_data = dynamic_map_data[dynamic_map_data.length-1];
            // 动态颜色映射
            var mapcolor=dynamic_map_data[0];
            // 基础颜色设置
            var color = function(d){
                if (d==0){
                    return 255;
                }
                else {
                    return 200-d*20;
                }
            };
            // tooltip
            var map_tooltip = d3.select("#my_map")
                .append("div")
                .style("opacity", 0)
                .attr("class", "map_tooltip")
                .style("background-color", "white")
                .style("border", "solid")
                .style("border-width", "1px")
                .style("border-radius", "5px")
                .style("padding", "10px")
            
            var mouseover = function(event,d) {
                d3.select(this)
                    .attr("fill","#44bd9c");

                if( final_data[d.properties.name] == 0){
                    return 0;
                }

                map_tooltip.style("opacity", 1)}
    
            var mousemove = function(event,d) {
                // console.log(final_data[d.properties.name]);
                if( final_data[d.properties.name] == 0){
                    return 0;
                }
                let temp_province = d.properties.name;
                let amount = final_data[temp_province];
                let detail_info = map_data[temp_province];
                let tip_height = 60 + 20*(amount-1);
                
                map_tooltip.style("opacity", 1);

                map_tooltip
                .html(function(d){
                    let show_info = temp_province+" <br/>共 "+amount+" 位 首辅";
                    for (let i=0;i<detail_info.length;i++)
                    { 
                        show_info=show_info+"<br/>"+detail_info[i].name+"\t"+detail_info[i].home_info;
                    }
                    return show_info;
                })
                .style("height",tip_height+"px")
                .style("left", (d3.pointer(event,this)[0]+30) + "px") // 90是最佳实践
                .style("top", (d3.pointer(event,this)[1]) + "px")
            }
            
            var mouseleave = function(event,d) {
                let tmp_color = color(mapcolor[d.properties.name]);

                d3.select(this)
                    .attr("fill","rgb("+ tmp_color +","+tmp_color+","+ tmp_color +")");

                if( final_data[d.properties.name] == 0){
                    return 0;
                }

                map_tooltip
                    .transition()
                    .duration(200)
                    .style("opacity", 0)
            }
            //定义地图的投影
            var projection = d3.geoMercator()    //d3.geo.mercator()    
                .center([107, 31])
                .scale(550)
                .translate([width*0.5, height/2*1.2]);

            //定义地形路径生成器 
            var path = d3.geoPath()    //d3.geo.path()
                .projection(projection);	//设定投影
            // 绘制地图
            map_group.selectAll("path")
				.data(root.features)
				.enter()
			    .append("path")
				.attr("class","province")
				.attr("z-index",1)
				.attr("fill", function(d,i){
                    if(mapcolor[d.properties.name]==undefined){
                        mapcolor[d.properties.name]=0;
					}
					let tmp_color = color(mapcolor[d.properties.name]);
					return "rgb("+ tmp_color +","+tmp_color+","+ tmp_color +")";
				})
				.attr("d", path);	//使用路径生成器

            d3.xml("./map/southchinasea.svg").then(function(xmlDocument) {
				map_group.html(function(d){
					return d3.select(this).html() + xmlDocument.getElementsByTagName("g")[0].outerHTML;
				});			
				d3.select("#southchinasea")
					.attr("transform","translate("+[width*0.7, height*0.66]+") scale(0.5)")
					.attr("class","southchinasea");
		    });
            // 地图图例
            // https://bl.ocks.org/duspviz-mit/9b6dce37101c30ab80d0bf378fe5e583
            var legend_h = 300, legend_w = 50;

            var legend = map_group.append("defs")
                .append("svg:linearGradient")
                .attr("id", "gradient")
                .attr("x1", "100%")
                .attr("y1", "0%")
                .attr("x2", "100%")
                .attr("y2", "100%")
                .attr("spreadMethod", "pad");

            legend.append("stop")
                .attr("offset", "0%")
                .attr("stop-color", "#000000")
                .attr("stop-opacity", 1);

            legend.append("stop")
                .attr("offset", "33%")
                .attr("stop-color", "#555555")
                .attr("stop-opacity", 1);

            legend.append("stop")
                .attr("offset", "66%")
                .attr("stop-color", "#787878")
                .attr("stop-opacity", 1);

            legend.append("stop")
                .attr("offset", "100%")
                .attr("stop-color", "#ffffff")
                .attr("stop-opacity", 1);
            // [width*0.7, height*0.66]
            map_group.append("rect")
                .attr("width", legend_w - 30)
                .attr("height", legend_h)
                .style("fill", "url(#gradient)")
                .attr("transform", `translate(${width*0.87},${height*0.2})`);

            var y = d3.scaleLinear()
                .range([300, 0])
                .domain([0, 10]);

            var yAxis = d3.axisRight()
                .scale(y)
                .ticks(5);

            map_group.append("g")
                .attr("class", "y axis")
                .attr("transform", `translate(${width*0.87+20},${height*0.2})`)
                .call(yAxis)
                .append("text")
                .attr("transform", "rotate(-90)")
                .attr("y", 0)
                .attr("dy", ".71em")
                // .style("text-anchor", "end")
                // .text("axis title");
            // 更新地图函数
            var transitionMap = function(i){
                mapcolor = dynamic_map_data[i];
                d3.select("#map").selectAll('path')
                    .data(root.features)
                    .transition()
                    .delay(100)
                    .duration(1000)
                    .attr('fill', function(d,i){
                        if(mapcolor[d.properties.name]==undefined){
                            mapcolor[d.properties.name]=0;
                        }
                        let tmp_color = color(mapcolor[d.properties.name]);
                            return "rgb("+ tmp_color +","+tmp_color+","+ tmp_color +")";
                    })
            };
            // 定时器
            let time = 1;
            let title = d3.select("#map")
                .append("text")
                .attr("id","title")
                .attr("transform","translate("+[width*0.48, height*0.95]+")")
                .attr("font-size","30px");
            title.text("永乐");
            let interval = setInterval(() => {
                if (time <= 13) {
                    transitionMap(time);
                    d3.select("#title").text(d=>title_list[time]);
                    time++;
                } else {
                    clearInterval(interval);
                    map_group.selectAll("path")
                        .data(root.features)
                        .on("mouseover",mouseover)
                        .on("mousemove",mousemove)
                        .on("mouseleave",mouseleave);
                }
            }, 1000);
        },
        /**
         * 获取事件函数，用于禁止子事件冒泡
         * https://blog.csdn.net/ming199481/article/details/81505367
         */
        getEvent(){
            if(window.event){return window.event;}
            var func = getEvent.caller;
            while(func != null){
                var arg0 = func.arguments[0];
                if(arg0){
                    if((arg0.constructor == Event || arg0.constructor == MouseEvent
                            || arg0.constructor == KeyboardEvent)
                        || (typeof(arg0) == "object" && arg0.preventDefault
                            && arg0.stopPropagation)){
                        return arg0;
                    }
                }
                func = func.caller;
            }
            return null;
        }
    }
      
})
</script>

<style>
.province {
    stroke: black;
    stroke-width: 1px;
}
		  
.southchinasea {
    stroke: black;
    stroke-width: 1px;
    fill: #fff;
}
div.map_tooltip {	
    position: absolute;			
    text-align: center;			
    width: 160px;					
    height: 80px;					
    padding: 2px;				
    font: 12px sans-serif;
    line-height: 20px;	
    border: 0px;	
    border-radius: 8px;			
    pointer-events: none;			
}
.axis text {
  font: 14px sans-serif;
}

.axis line, .axis path {
  fill: none;
  stroke: #000;
  shape-rendering: crispEdges;
}
</style>