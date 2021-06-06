<template>
  <div id="my_title"></div>
</template>

<script>
import { defineComponent } from "vue";
import * as d3 from 'd3';

export default defineComponent({
  data() {
    return {}
  },
  mounted(){
    this.drawTitle();
  },

  methods:{
    /**
     * 绘制标题
     */
    drawTitle(){
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
      var svg = d3.select("#my_title")
          .append("svg")
          .attr("width", width + margin.left + margin.right)
              .attr("height", height + margin.top + margin.bottom)
              .append("g")
            .attr("transform",
             "translate(" + margin.left + "," + margin.top + ")");
      // 绘制标题
      svg.append('text')
            .attr('class', 'title')
            .attr('x', width / 2)
            .attr('y', height / 3)
            .text('大明首辅');
    
      svg.append('text')
            .attr('class', 'sub-title')
            .attr('x', width / 2)
            .attr('y', (height / 3) + (height / 5))
            .text('观察录');
    }
  }

})
</script>

<style>
#my_title .title {
  font-size:120px;
  text-anchor: middle;
}

#my_title .sub-title {
  font-size:80px;
  text-anchor: middle;
}
</style>
