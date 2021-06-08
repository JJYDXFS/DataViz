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
                纵轴代表该任首辅在位的任职时间<br/>
                可以发现一朝天子一朝臣，所言不虚<br/>
                如果你在两堆颜色之间发现一个“第三色”<br/>
                说明这可能是一位两朝元老哦
            </section>
            <section class="step">
                <div class="title" >Part3 动态地图</div>
                那么有明一代的首辅们都来自哪里呢？右侧是自永乐朝始，历代首辅的籍贯。
                等动画加载完成后，移动到感兴趣的省份上查看那里出身的首辅吧<br/>
                根据我们的统计，“贡献”首辅最多的是江西省和浙江省<br/>
                各出了10位首辅大人
            </section>
            <section class="step">
                <div class="title" >Part4 学历桑基图</div>
                首辅作为明代文官之路的巅峰，是“学而优则仕”的最佳体现<br/>
                在明代，科举制度自下而上分为三层<br/>
                通过殿试的考生将依名次被分别授予<br/>
                一甲、二甲和三甲的出身<br/>
                一甲只有三人：状元、榜眼、探花<br/>
                二甲加起来则有二三百人<br/>
                二甲赐进士出身，三甲赐同进士出身<br/>
            </section>
            <section class="step">
                <div class="title" >Part 5 谥号树图</div>
                干得好的首辅在死后将会得到来自朝廷的感谢——谥号<br/>
                明代的首辅大都能得到以“文”字打头的谥号<br/>
                而历代文官谥号之最莫过于“文正”，相传李东阳在得知自己的谥号会被定为文正后，激动地从病榻起身开始磕头
            </section>
            <section class="step">
                <div class="title" >Part 6</div>
                Hello, section five?
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
import OriginSankey from './components/OriginSankey.vue'
import CirclePacking from './components/CirclePacking.vue'

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
    OriginSankey,
    CirclePacking,
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
      /**
       * 教程参考
       * https://vallandingham.me/scroller.html
       */
      this.initScroller();
      // 当活动section改变时，将调用不同的激活函数
      activateFunctions[0] = this.showTitle;
      activateFunctions[1] = this.showScatter;
      activateFunctions[2] = this.showHomeMap;
      activateFunctions[3] = this.showOriginSankey;
      activateFunctions[4] = this.showCirclePacking;
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
       * 激活对应的数据可视化图表
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
      },
      showOriginSankey(){
          this.comName = "OriginSankey";
      },
      showCirclePacking(){
          this.comName = "CirclePacking";
      },
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
    font-size: 16px;
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
    top: 40px;
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
