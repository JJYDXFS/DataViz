
<template>
<div id="input_box">
        <el-row class="demo-autocomplete">
        <el-col :span="15">
            <div class="sub-title">通过姓名检索首辅</div>
            <el-autocomplete
            class="inline-input"
            v-model="state1"
            :fetch-suggestions="querySearch"
            placeholder="请输入首辅姓名"
            @select="handleSelect"
            ></el-autocomplete>
        </el-col>
        </el-row>
    </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import axios from 'axios'

export default defineComponent({
  data(){
    return {
    }
  },
  methods:{
    handleSelect (item) {
      var thisInstence = this;
      axios.get("http://42.193.108.195:5000/api/get_pm_info",{params:{name:item.value}})
                .then((res) => {
                  thisInstence.$parent.$refs.myviz.transRadarChart(res['data']['result']);
      });
    },
  },
  setup() {
    const primer_minister = ref([]);
    const querySearch = (queryString, cb) => {
      var results = queryString
        ? primer_minister.value.filter(createFilter(queryString))
        : primer_minister.value;
      // 调用 callback 返回建议列表的数据
      cb(results);
    };
    const createFilter = (queryString) => {
      return (primer_minister) => {
        return (
          primer_minister.value.toLowerCase().indexOf(queryString.toLowerCase()) ===
          0
        );
      };
    };
    const loadAll = () => {
      return [
        {value: '曹鼐'}, {value: '陈文'}, {value: '陈循'}, {value: '成基命'}, 
        {value: '范复粹'}, {value: '费宏'}, {value: '高拱'}, {value: '高榖'}, 
        {value: '顾秉谦'}, {value: '顾鼎臣'}, {value: '韩爌'}, {value: '胡广'}, 
        {value: '黄淮'}, {value: '黄立极'}, {value: '蒋德璟'}, {value: '蒋冕'}, 
        {value: '解缙'}, {value: '孔贞运'}, {value: '来宗道'}, {value: '李标'}, 
        {value: '李春芳'}, {value: '李东阳'}, {value: '李时'}, {value: '李廷机'}, 
        {value: '李贤'}, {value: '梁储'}, {value: '刘吉'}, {value: '刘健'}, 
        {value: '刘一燝'}, {value: '毛纪'}, {value: '彭时'}, {value: '商辂'}, 
        {value: '申时行'}, {value: '沈一贯'}, {value: '施凤来'}, {value: '万安'}, 
        {value: '王家屏'}, {value: '王锡爵'}, {value: '魏藻德'}, {value: '温体仁'}, 
        {value: '夏言'}, {value: '徐阶'}, {value: '徐溥'}, {value: '徐有贞'}, 
        {value: '许彬'}, {value: '严嵩'}, {value: '杨溥'}, {value: '杨荣'}, 
        {value: '杨士奇'}, {value: '杨廷和'}, {value: '杨一清'}, {value: '叶向高'}, 
        {value: '翟銮'}, {value: '张璁'}, {value: '张居正'}, {value: '张四维'}, 
        {value: '张至发'}, {value: '赵志皋'}, {value: '周延儒'}, {value: '朱赓'}, 
        {value: '朱国祯'},
      ];
    };
    onMounted(() => {
      primer_minister.value = loadAll();
    });
    return {
      primer_minister,
      state1: ref(''),
      state2: ref(''),
      querySearch,
      createFilter,
      loadAll,
      //handleSelect,
    };
  },
});
</script>

<style>
@import 'element-theme-chalk';
</style>