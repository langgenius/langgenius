import type { FC } from 'react'
import React from 'react'
import { useTranslation } from 'react-i18next'

import Split from '../_base/components/split'
import ResultPanel from '../../run/result-panel'
import InputNumberWithSlider from '../_base/components/input-number-with-slider'
import type { LoopNodeType } from './types'
import useConfig from './use-config'
import type { NodePanelProps } from '@/app/components/workflow/types'
import ConditionWrap from './components/condition-wrap'
import Field from '@/app/components/workflow/nodes/_base/components/field'
import BeforeRunForm from '@/app/components/workflow/nodes/_base/components/before-run-form'
import formatTracing from '@/app/components/workflow/run/utils/format-log'

import { useLogs } from '@/app/components/workflow/run/hooks'

const i18nPrefix = 'workflow.nodes.loop'

const Panel: FC<NodePanelProps<LoopNodeType>> = ({
  id,
  data,
}) => {
  const { t } = useTranslation()

  const {
    readOnly,
    inputs,
    childrenNodeVars,
    loopChildrenNodes,
    isShowSingleRun,
    hideSingleRun,
    runningStatus,
    handleRun,
    handleStop,
    runResult,
    loopRunResult,
    handleAddCondition,
    handleUpdateCondition,
    handleRemoveCondition,
    handleToggleConditionLogicalOperator,
    handleAddSubVariableCondition,
    handleRemoveSubVariableCondition,
    handleUpdateSubVariableCondition,
    handleToggleSubVariableConditionLogicalOperator,
    handleUpdateLoopCount,
  } = useConfig(id, data)

  const nodeInfo = formatTracing(loopRunResult, t)[0]
  const logsParams = useLogs()

  return (
    <div className='mt-2'>
      <div>
        <Field
          title={<div className='pl-3'>{t(`${i18nPrefix}.breakCondition`)}</div>}
        >
          <ConditionWrap
            nodeId={id}
            readOnly={readOnly}
            handleAddCondition={handleAddCondition}
            handleRemoveCondition={handleRemoveCondition}
            handleUpdateCondition={handleUpdateCondition}
            handleToggleConditionLogicalOperator={handleToggleConditionLogicalOperator}
            handleAddSubVariableCondition={handleAddSubVariableCondition}
            handleRemoveSubVariableCondition={handleRemoveSubVariableCondition}
            handleUpdateSubVariableCondition={handleUpdateSubVariableCondition}
            handleToggleSubVariableConditionLogicalOperator={handleToggleSubVariableConditionLogicalOperator}
            availableNodes={loopChildrenNodes}
            availableVars={childrenNodeVars}
            conditions={inputs.break_conditions || []}
            logicalOperator={inputs.logical_operator!}
          />
        </Field>
        <Split />
        <div className='mt-2'>
          <Field
            title={<div className='pl-3'>{t(`${i18nPrefix}.loopMaxCount`)}</div>}
          >
            <div className='px-3 py-2'>
              <InputNumberWithSlider
                min={1}
                max={100}
                value={inputs.loop_count}
                onChange={(val) => {
                  const roundedVal = Math.round(val)
                  handleUpdateLoopCount(Number.isNaN(roundedVal) ? 1 : roundedVal)
                }}
              />
            </div>
          </Field>
        </div>
      </div>
      {/* Error handling for the Loop node is currently not considered. */}
      {/* <div className='px-4 py-2'>
        <Field title={t(`${i18nPrefix}.errorResponseMethod`)} >
          <Select items={responseMethod} defaultValue={inputs.error_handle_mode} onSelect={changeErrorResponseMode} allowSearch={false}>
          </Select>
        </Field>
      </div> */}
      {isShowSingleRun && (
        <BeforeRunForm
          nodeName={inputs.title}
          onHide={hideSingleRun}
          forms={[]}
          runningStatus={runningStatus}
          onRun={handleRun}
          onStop={handleStop}
          {...logsParams}
          result={
            <ResultPanel {...runResult} showSteps={false} nodeInfo={nodeInfo} {...logsParams} />
          }
        />
      )}
    </div>
  )
}

export default React.memo(Panel)