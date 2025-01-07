'use client'
import React, { useState } from 'react'
import { useTranslation } from 'react-i18next'
import {
  RiDeleteBinLine,
  RiEqualizer2Line,
  RiErrorWarningFill,
  RiInstallLine,
  RiLoader2Line,
} from '@remixicon/react'
import { Group } from '@/app/components/base/icons/src/vender/other'
import AppIcon from '@/app/components/base/app-icon'
import Switch from '@/app/components/base/switch'
import Button from '@/app/components/base/button'
import Indicator from '@/app/components/header/indicator'
import ActionButton from '@/app/components/base/action-button'
import Tooltip from '@/app/components/base/tooltip'
import cn from '@/utils/classnames'

type Props = {
  icon?: any
  providerName?: string
  toolName?: string
  showSwitch?: boolean
  switchValue?: boolean
  onSwitchChange?: (value: boolean) => void
  onDelete?: () => void
  noAuth?: boolean
  onAuth?: () => void
  isError?: boolean
  errorTip?: any
  uninstalled?: boolean
  isInstalling?: boolean
  onInstall?: () => void
  open: boolean
}

const ToolItem = ({
  open,
  icon,
  providerName,
  toolName,
  showSwitch,
  switchValue,
  onSwitchChange,
  onDelete,
  noAuth,
  onAuth,
  uninstalled,
  isInstalling,
  onInstall,
  isError,
  errorTip,
}: Props) => {
  const { t } = useTranslation()
  const providerNameText = providerName?.split('/').pop()
  const isTransparent = uninstalled || isError
  const [isDeleting, setIsDeleting] = useState(false)

  return (
    <div className={cn(
      'group p-1.5 pr-2 flex items-center gap-1 bg-components-panel-on-panel-item-bg border-[0.5px] border-components-panel-border-subtle rounded-lg shadow-xs cursor-default hover:bg-components-panel-on-panel-item-bg-hover hover:shadow-sm',
      open && 'bg-components-panel-on-panel-item-bg-hover shadow-sm',
      isDeleting && 'hover:bg-state-destructive-hover border-state-destructive-border shadow-xs',
    )}>
      {icon && (
        <div className={cn('shrink-0', isTransparent && 'opacity-50')}>
          {typeof icon === 'string' && <div className='w-7 h-7 bg-cover bg-center border-[0.5px] border-components-panel-border-subtle bg-background-default-dodge rounded-lg' style={{ backgroundImage: `url(${icon})` }} />}
          {typeof icon !== 'string' && <AppIcon className='w-7 h-7 border-[0.5px] border-components-panel-border-subtle bg-background-default-dodge rounded-lg' size='xs' icon={icon?.content} background={icon?.background} />}
        </div>
      )}
      {!icon && (
        <div className={cn(
          'flex items-center justify-center w-7 h-7 rounded-md border-[0.5px] border-components-panel-border-subtle bg-background-default-subtle',
        )}>
          <div className='flex w-5 h-5 items-center justify-center opacity-35'>
            <Group className='text-text-tertiary' />
          </div>
        </div>
      )}
      <div className={cn('pl-0.5 grow truncate', isTransparent && 'opacity-50')}>
        <div className='text-text-tertiary system-2xs-medium-uppercase'>{providerNameText}</div>
        <div className='text-text-secondary system-xs-medium'>{toolName}</div>
      </div>
      <div className='hidden group-hover:flex items-center gap-1'>
        {!noAuth && !isError && !uninstalled && (
          <ActionButton>
            <RiEqualizer2Line className='w-4 h-4' />
          </ActionButton>
        )}
        <div
          className='p-1 rounded-md text-text-tertiary cursor-pointer hover:text-text-destructive'
          onClick={(e) => {
            e.stopPropagation()
            onDelete?.()
          }}
          onMouseOver={() => setIsDeleting(true)}
          onMouseLeave={() => setIsDeleting(false)}
        >
          <RiDeleteBinLine className='w-4 h-4' />
        </div>
      </div>
      {!isError && !uninstalled && !noAuth && showSwitch && (
        <div className='mr-1' onClick={e => e.stopPropagation()}>
          <Switch
            size='md'
            defaultValue={switchValue}
            onChange={onSwitchChange}
          />
        </div>
      )}
      {!isError && !uninstalled && noAuth && (
        <Button variant='secondary' size='small' onClick={onAuth}>
          {t('tools.notAuthorized')}
          <Indicator className='ml-2' color='orange' />
        </Button>
      )}
      {!isError && uninstalled && (
        <Button
          className={cn('flex items-center')}
          size='small'
          variant='secondary'
          disabled={isInstalling}
          onClick={(e) => {
            e.stopPropagation()
            onInstall?.()
          }}
        >
          {!isInstalling ? t('workflow.nodes.agent.pluginInstaller.install') : t('workflow.nodes.agent.pluginInstaller.installing')}
          {!isInstalling ? <RiInstallLine className='size-4 ml-1' /> : <RiLoader2Line className='size-4 ml-1 animate-spin' />}
        </Button>
      )}
      {isError && (
        <Tooltip
          popupContent={errorTip}
          needsDelay
        >
          <div>
            <RiErrorWarningFill className='w-4 h-4 text-text-destructive' />
          </div>
        </Tooltip>
      )}
    </div>
  )
}

export default ToolItem