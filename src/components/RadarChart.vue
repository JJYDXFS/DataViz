<template>
    <div id="info">
        <div id="my_radar">

        </div>
        <div id="intro">
            个人简介
        </div>
    </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import * as d3 from 'd3';
import { RadarChart } from '../js/radarChart.js'
import axios from 'axios'

export default defineComponent({
    setup() {
        // 有关svg的数据
        /* 常量
        ---------------------------------------------------------------------------------------------------*/
        const margin = {top: 100, right: 200, bottom: 30, left: 100};
        const w_width = ref(window.innerWidth
            || document.documentElement.clientWidth
            || document.body.clientWidth);

        const w_height = ref(window.innerHeight
            || document.documentElement.clientHeight
            || document.body.clientHeight);

        const width = w_width*0.87 - margin.left - margin.right;
        const height = w_height*0.9 - margin.top - margin.bottom;

        const radarChartOptions = {
			w: 290,
			h: 350,
			margin: margin,
			maxValue: 20,
			levels: 6,
			roundStrokes: false,
			color: d3.scaleOrdinal().range(["#3366CC", "#FF9966"]),
			format: '.2f',
			legend: { title: '与平均值对比情况', translateX: 100, translateY: 40 },
			unit: ''
		};
        const initRadarChart = () => {
            // 初始化信息
            let data = [
				{ name: '该首辅个人信息',
					axes: [
                        {axis: '任期总长（年）', value: 3.09},
						{axis: '首次上任年龄（5年）', value: 44/5},
						{axis: '享年（5年）', value: 48/5},
						//{axis: '出任首辅次数', value: 1}
					]
				},
				{ name: '明代首辅平均值(61人)',
					axes: [
                        {axis: '任期总长（年）', value: 3.60},
						{axis: '首次上任年龄（5年）', value: 57.52/5},
						{axis: '享年（5年）', value: 70.16/5},
						//{axis: '出任首辅次数', value: 1.33}
					]
				}
			];

			let radar = RadarChart("#my_radar", data, radarChartOptions);
        };
        const transRadarChart = (res) => {
            // 初始化信息
            let data = [
				{ name: '该首辅个人信息',
					axes: [
                        {axis: '任期总长（年）', value: res.scale},
						{axis: '首次上任年龄（5年）', value: res.begin_age/5},
						{axis: '享年（5年）', value: res.age/5},
						//{axis: '出任首辅次数', value: 1}
					]
				},
				{ name: '明代首辅平均值(61人)',
					axes: [
                        {axis: '任期总长（年）', value: 3.60},
						{axis: '首次上任年龄（5年）', value: 57.52/5},
						{axis: '享年（5年）', value: 70.16/5},
						//{axis: '出任首辅次数', value: 1.33}
					]
				}
			];

			let radar = RadarChart("#my_radar", data, radarChartOptions);
        }
        onMounted(() => {
            initRadarChart();
            });
            return {
            initRadarChart,
            transRadarChart,
        };
    },
    data() {
        return {
            radar:null,
        }
    },

})
</script>

<style>
@import url("//unpkg.com/element-plus/lib/theme-chalk/index.css");

#my_radar {
    float: left;
}

#intro {
    float: left;
}
</style>