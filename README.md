# Handdrawn Icons · 手绘风图标库

Hand-drawn, lightly dimensional icons for AI skills, agents, workflows and web interfaces.

本项目旨在长期维护可复用的手绘轻拟物图标。**优先保留插画质感，不强制将插画简化成线性 SVG**。

## Visual direction

- 黑白粗线条、圆润且略微不规则的手绘轮廓
- 有适度的实心黑色区域、结构层次与物体辨识度
- 图标本身使用透明背景，底色由使用方配置
- 不要批量添加右上角三条装饰线
- 必须保留图案完整轮廓和安全留白，尤其是底部
- 目标展示尺寸：32 / 40 / 48 / 64 px

完整创作与验收规则请查看 [STYLE_GUIDE.md](STYLE_GUIDE.md)。

## Repository structure

```text
assets/
  hand-drawn/
    v1/
      agent.webp
      translate.webp
      ...
sources/
  hand-drawn/
    v1/              # 保留可编辑/高清 PNG 母版（后续添加）
manifest.json         # 素材清单
examples/
  react/
    SkillIcon.tsx      # React / TypeScript 示例
STYLE_GUIDE.md
```

> **当前状态：** 仓库先初始化规范和 React 使用方式。首批 12 张 WebP 尚待完整性与透明背景检查，避免发布先前裁切时出现底部缺边的版本。资源与清单会在素材验收后补齐。

## React usage

将 `assets/` 放到项目 `public/illustrations/assets/` 目录，随后使用 [SkillIcon.tsx](examples/react/SkillIcon.tsx)。

```tsx
<SkillIcon name="agent" size={40} background="#DBEAFE" />
<SkillIcon name="translate" size={48} background="#FCE7F3" />
<SkillIcon name="knowledge" size={40} background="transparent" />
```

组件的图片地址约定为：

```text
/illustrations/assets/hand-drawn/v1/<name>.webp
```

可调整 `basePath` 以适配不同项目的静态资源托管方式。

## Adding an icon

1. 按 [STYLE_GUIDE.md](STYLE_GUIDE.md) 单独绘制高清完整图案。
2. 导出透明 PNG 母版和透明 lossless WebP。
3. 验证透明通道及 32/40/48/64px 下的可读性，确保四边不截断。
4. 按风格、版本存入 `assets/<style>/vN/`，更新 `manifest.json` 和预览图。
5. 不直接覆盖已经发布的版本；保持稳定 ID。

## License

许可方案尚未确定。公开仓库不等于素材已采用开源许可证；如需第三方复用、再分发，请先明确授权。
