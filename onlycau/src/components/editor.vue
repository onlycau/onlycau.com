
<template>
    <div>
        <div ref="editor" style="text-align:left"></div>
    </div>
</template>

<script>
    import E from 'wangeditor'
    export default {
      name: 'editor',
      data () {
        return {
          editorContent: '',
          editor:'',
        }
      },
      methods: {
        getContent: function () {
            alert(this.editorContent)
        }
      },
      mounted() {
        this.editor = new E(this.$refs.editor)
        this.editor.customConfig.onchange = (html) => {
          this.editorContent = html
        }
        this.editor.create()
      }
    }
</script>

<style scoped>
</style>