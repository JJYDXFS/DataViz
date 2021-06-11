import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import App from './App.vue'
import InputWithSug from './components/InputWithSug.vue'
import RadarChart from './components/RadarChart.vue'

import './index.css'

const app = createApp(App);
app.use(ElementPlus);
app.mount("#app");

// // 使用element-ui
// const app = createApp(RadarChart)
// app.use(ElementPlus);
// // 挂载根组件App.vue
// app.mount('#app')
