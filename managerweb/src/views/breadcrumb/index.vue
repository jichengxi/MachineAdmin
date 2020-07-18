<template>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>1</el-breadcrumb-item>
      <el-breadcrumb-item>2</el-breadcrumb-item>
      <el-breadcrumb-item>3</el-breadcrumb-item>
    </el-breadcrumb>
</template>

<script>
export default {
  //
}
</script>

<style lang="scss">
  .el-breadcrumb{
    font-size: 14px;
    line-height: 30px;
  }
</style>
