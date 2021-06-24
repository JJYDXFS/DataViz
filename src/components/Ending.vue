<template>
  <div id="my_ending">
    <div class="refer">
      <h3 class="refer-title">参考资料</h3>
      <p><a href="https://ctext.org/searchbooks.pl?if=gb&remap=gb&searchu=%E6%98%8E%E5%AE%9E%E5%BD%95" target="_blank">《明实录》</a></p>
      <p><a href="https://ctext.org/wiki.pl?if=gb&res=706630" target="_blank">《大明会典》</a></p>
      <p><a href="https://ctext.org/wiki.pl?if=gb&res=410835" target="_blank">《明史》</a></p>
      <p><a href="https://baike.baidu.com/reference/1080773/6711rzSlvDTwa92ek81yVUJZsicKrw3IZPQ2JgH_3_jbyT4A9gfaYurn9RmjrqHP1_ONFgsY8ZunIzsvZ_Xv8WcVxNfsstCq7WG3aDUA" target="_blank">《明史·宰辅年表》</a></p>
      <p><a href="https://ctext.org/lost-book-of-zhou/shi-fa/zh" target="_blank">《逸周书·谥法解》</a></p>
      <p><a href="https://ctext.org/wiki.pl?if=gb&res=573006" target="_blank">《谥法通考》</a></p>
      <p><a href="https://ctext.org/wiki.pl?if=gb&chapter=312717" target="_blank">《明会要·卷 十九》</a></p>
      <p><a href="http://www.mingchaonaxieshier.com/" target="_blank">《明朝那些事儿》</a></p>
      <p><a href="http://www.360doc.com/userhome.aspx?userid=20226523&cid=115" target="_blank">《明朝、清朝各科殿试金榜（进士）名录》</a></p>
      <p><a href="http://www.onegreen.net/maps/List/List_1231.html" target="_blank">《明朝地图集》</a></p>
    </div>
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
    this.drawEnding();
  },

  methods:{
    /**
     * 绘制标题
     */
    drawEnding(){
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
      var svg = d3.select("#my_ending")
          .append("svg")
          .attr("width", width + margin.left + margin.right)
              .attr("height", height + margin.top + margin.bottom)
              .append("g")
            .attr("transform",
             "translate(" + margin.left + "," + margin.top + ")");

      var rects = svg.append("rect")
					.attr("class", "bar")
          .attr("x", width*0.25)
					.attr("y", height * 0.15);
					
			rects.attr("height", 20)
					.transition()
					.duration(5000)
					.attr("width", width*0.43);

      var mytext = svg.append("text")
					.attr("class", "typing")
          .attr("x", width*0.40)
					.attr("y", height * 0.125)
          .text("观察进度保存中...")
    }
  }

})
</script>

<style>
#my_ending .title {
  text-align:center;
  margin-top: 10px;
  color:black;
  font-size:120px;
  text-anchor: middle;
}

#my_ending .sub-title {
  font-size:80px;
  text-anchor: middle;
}

#my_ending .refer {
  text-align: center;
  line-height: 75%;
}

#my_ending .refer-title{
  margin-bottom: 5%;
}

.bar{
  fill:rgb(43, 106, 132);
}

.text{
  font-size: 16px;
}
</style>
