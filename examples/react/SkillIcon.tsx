import type { CSSProperties } from 'react';

export const skillIconNames = [
  'code', 'search', 'knowledge', 'analytics', 'agent', 'writing',
  'workflow', 'creative', 'data', 'security', 'translate', 'automate',
] as const;

export type SkillIconName = (typeof skillIconNames)[number];

type SkillIconProps = {
  name: SkillIconName;
  size?: number;
  background?: string;
  radius?: number;
  basePath?: string;
  version?: string;
  className?: string;
  style?: CSSProperties;
};

export function SkillIcon({
  name,
  size = 40,
  background = '#F3F4F6',
  radius = 10,
  version = 'v1',
  basePath = '/illustrations/assets',
  className,
  style,
}: SkillIconProps) {
  const src = `${basePath}/hand-drawn/${version}/${name}.webp`;

  return (
    <span
      className={className}
      style={{
        width: size,
        height: size,
        flexShrink: 0,
        display: 'inline-flex',
        alignItems: 'center',
        justifyContent: 'center',
        borderRadius: radius,
        background,
        ...style,
      }}
    >
      <img
        src={src}
        alt=""
        width={Math.round(size * 0.86)}
        height={Math.round(size * 0.86)}
        decoding="async"
        draggable={false}
        style={{ display: 'block', objectFit: 'contain' }}
      />
    </span>
  );
}
