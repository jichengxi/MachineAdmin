<template>
<!--    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">-->
<!--      <el-radio-button :label="false">展开</el-radio-button>-->
<!--      <el-radio-button :label="true">收起</el-radio-button>-->
<!--    </el-radio-group>-->
    <el-menu default-active="1-4-1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse"
             background-color="#EFD37D"
             text-color="#000"
             active-text-color="#3CB3E6" style="width: 100%">
      <el-menu-item index="1">
        <i class="el-icon-present"></i>
        <span slot="title">Dashboard</span>
      </el-menu-item>
      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-coin"></i>
          <span slot="title">物理机</span>
        </template>
<!--        选项卡-->
        <el-menu-item-group>
          <el-menu-item index="2-1">查询</el-menu-item>
          <el-menu-item index="2-2">操作</el-menu-item>
        </el-menu-item-group>
      </el-submenu>

      <el-submenu index="3">
        <template slot="title">
          <i class="el-icon-connection"></i>
          <span slot="title">虚拟机</span>
        </template>
        <el-menu-item-group>
          <span slot="title">分组一</span>
          <el-menu-item index="2-1">选项1</el-menu-item>
          <el-menu-item index="2-2">选项2</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2">
          <el-menu-item index="2-3">选项3</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="2-4">
          <span slot="title">选项4</span>
          <el-menu-item index="2-4-1">选项1</el-menu-item>
        </el-submenu>
      </el-submenu>
      <el-menu-item index="4">
        <i class="el-icon-setting"></i>
        <span slot="title">导航四</span>
      </el-menu-item>
    </el-menu>
</template>

<style lang="scss">
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    /*width: 200px;*/
    min-height: 400px;
  }
</style>

<script>
export default {
  data () {
    return {
      isCollapse: false,
      screenWidth: document.body.clientWidth
    }
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  },
  mounted () {
    const that = this
    // console.log(this)
    window.onresize = () => {
      return (() => {
        // console.log(document.body.clientWidth)
        window.screenWidth = document.body.clientWidth
        that.screenWidth = window.screenWidth
      })()
    }
  },
  watch: {
    screenWidth: {
      immediate: true,
      handler: function (newval) {
        // console.log(newval)
        if (newval < 1200 && this.isCollapse !== true) {
          // console.log(this.isCollapse)
          this.isCollapse = !this.isCollapse
          // this.$emit('fromSidebar', this.isCollapse)
        } else if (newval > 1200 && this.isCollapse !== false) {
          // console.log(this.isCollapse)
          this.isCollapse = !this.isCollapse
          // this.$emit('fromSidebar', this.isCollapse)
        }
      }
    }
  }

}
</script>
