<template>
  <div id="graphic">
        <div id="sections">
            <section class="step">
                <div class="title" >Part1 介绍</div>
                这一部分将放置一些关于 “首辅是什么” 的介绍<br/><br/>以及本作品的创作动机和意义
            </section>
            <section class="step">
                <div class="title" >Part2 散点图展开</div>
                我们整理了从黄淮到魏藻德在内的87任、共67位首辅<br/>
                右侧是时间散点图<br/>
                横轴刻度代表了皇权更替的时间点<br/>
                纵轴代表该任首辅在位的任职时间
            </section>
            <section class="step">
                <div class="title" >Part3 动态地图</div>
                那么有明一代的首辅们都来自哪里呢？右侧是自永乐朝始，历代首辅的籍贯。
                等动画加载完成后，移动到感兴趣的省份上查看那里出身的首辅吧
            </section>
            <section class="step">
                <div class="title" >Four</div>
                Hello, section four
            </section>
            <section class="step">
                <div class="title" >Five</div>
                Hello, section five
            </section>
        </div>
        <div id="vis">
            <transition mode="out-in">
                <component v-bind:is="comName"></component>
            </transition>
        </div>
    </div>
</template>

<script>
import {scroller} from '../src/js/scroller.js'
import Title from './components/Title.vue'
import Scatter from './components/Scatter.vue'
import HomeMap from './components/HomeMap.vue'

import * as d3 from 'd3';

var activateFunctions = [];
var updateFunctions = [];
var lastIndex = -1;
var activeIndex = 0;

export default {
  name: 'App',
  components: {
    Scatter,
    Title,
    HomeMap,
    // Wordcloud
  },
  data(){
    // 定义激活函数列表
    // var activateFunctions = [];
    // 定义刷新函数列表
    // var updateFunctions = [];
    return{
        comName:"Title",
    };
  },
  mounted(){
      this.initScroller();
      // 当活动section改变时，将调用不同的激活函数
      activateFunctions[0] = this.showTitle;
      activateFunctions[1] = this.showScatter;
      activateFunctions[2] = this.showHomeMap;
      activateFunctions[3] = this.showTitle;
      activateFunctions[4] = this.showTitle;
      activateFunctions[5] = this.showTitle;
  },
  methods:{
      initScroller(){
        var comp = this;
        var scroll = scroller()
            .container(d3.select("#graphic"));
        // 逐步调用
        scroll(d3.selectAll('.step'));
            
        // 设置事件句柄
        scroll.on('active', function (index){
            // 高亮当前section
            d3.selectAll('.step')
            .style('opacity', function (d, i) { return i === index ? 1 : 0.1; });
                
            comp.activateViz(index);
        });
      },

      /**
       * 激活
       * 
       * @param index - 激活部分的下标
      */
      activateViz(index) {
          activeIndex = index;
          var sign = (activeIndex - lastIndex) < 0 ? -1 : 1;
          var scrolledSections = d3.range(lastIndex + sign, activeIndex + sign, sign);
          scrolledSections.forEach(function (i) {
              activateFunctions[i]();
            });
              
        lastIndex = activeIndex;
      },
      showTitle(){
          this.comName = "Title";
      },
      showScatter(){
          this.comName = "Scatter";
      },
      showHomeMap(){
          this.comName = "HomeMap";
      }
  }
}
</script>

<style>
#sections{
    position: relative;
    display: inline-block;
    width: 17%;
    top: 0px;
    z-index: 90;
    margin-left: 5%;
}

.step{
    margin-bottom: 200px;
}

.title{
    font-size: large;
    font-family: Arial, Helvetica, sans-serif;
}

#vis{
    display: inline-block;
    position: fixed;
    top: 60px;
    z-index: 1;
    margin-left: 2%;

    height: 600px;
    width: 600px;
    /* background-color: #ddd; */
}
/* 组件过渡样式
 * https://blog.csdn.net/weixin_42218847/article/details/81481782
 */
.v-enter,.v-leave-to{
    opacity: 0;
    transform: translateX(150px);
}
        
.v-enter-active,.v-leave-active{
    transition: all 0.5s ease;
}
</style>
