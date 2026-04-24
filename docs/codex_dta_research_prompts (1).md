# Codex 云端 DTA 研究提示词手册

这份文档把前面讨论过的核心提示词整理成一套可直接复制使用的 Markdown 手册，适用于：

- 任务：drug-target affinity prediction
- 数据集：Davis / KIBA
- 重点：cold-start generalization
- 方式：Codex Cloud 同一个 thread 持续推进
- 目标：从学习、选创新、跑实验，到生成论文初稿

---

## 使用原则

1. **始终在同一个 cloud thread 里继续。**
2. **默认不创建 PR。**
3. **先学习，再选创新，再实现，再实验，再写稿。**
4. **不要把 placeholder run、文档产出、空表格当成实验结果。**
5. **所有创新必须服务于一条主线。**
6. **避免 generic MLP / gate / generic attention / generic fusion 这种“纯加容量”式创新。**
7. **重点盯住 cold-drug / cold-target，不把 random split 当主结果。**

---

## 0. 通用开头模板

后面大多数 prompt 都建议先加这一句：

```text
Continue in this same cloud thread.
Do not create a PR yet.
```

---

## 1. 总控版：让 Codex 自主完成从学习到论文初稿的全流程

```text
Continue in this same cloud thread.
Do not create a PR yet.

From now on, work as an autonomous research agent.
Your job is to complete the full research workflow end-to-end, from learning and innovation selection to implementation, experiments, and manuscript drafting.

Do not wait for user confirmation between substeps.
Do not stop after planning, drafting, or placeholder runs.
Do not treat document production alone as completion.

Primary objective:
Produce a credible first manuscript draft supported by real executable experiments whenever feasible.

Project scope is fixed:
- Task: drug-target affinity prediction
- Datasets: Davis and KIBA only
- Main focus: cold-start generalization only
- Primary setting: cold-drug
- Secondary setting: cold-target
- Optional stronger evidence: cold-both if feasible
- Literature scope: 2024-2026 only
- Research style: one single storyline, two core innovations, one incremental innovation
- Baseline preference: recent, lightweight, reproducible, easy to modify
- Avoid generic module stitching

Global operating rules:
1. Think proactively within scope.
2. If one idea looks trivial, reject it and propose a stronger mechanism-driven alternative.
3. If one path is blocked, continue all remaining non-blocked work.
4. Escalate weak baselines, weak controls, weak ablations, and weak claims instead of silently proceeding.
5. Never invent metrics, citations, datasets, baselines, or results.
6. Never treat placeholder runtime or placeholder output as experimental evidence.
7. Never optimize for flashy architecture changes.
8. Prefer mechanism-driven, lightweight, ablation-friendly ideas.
9. Everything must belong to one coherent causal storyline.
10. Do not create a PR unless explicitly asked.

Research philosophy:
- The paper must not be based on generic capacity increase.
- Do not use MLP/gate/attention/fusion changes unless they are clearly tied to a specific cold-start failure mechanism.
- Every proposed innovation must answer:
  a. what failure mode it targets,
  b. why it should help cold-start generalization,
  c. why it is more than generic capacity increase,
  d. what decisive control and ablation prove this.

Phased workflow:
Phase 0: Learn first
Phase 1: Select the innovation storyline
Phase 2: Unblock real runtime and reproduce the baseline
Phase 3: Implement the selected innovation
Phase 4: Run comparison experiments and ablations
Phase 5: Write the manuscript draft

You must execute all phases autonomously in order.

====================
PHASE 0: LEARNING
====================

Study 2024-2026 papers only, focusing on DTA and closely related ML ideas relevant to cold-start generalization.

Goals:
1. Learn how recent papers frame publishable innovation.
2. Learn how Davis/KIBA cold-start settings are defined and evaluated.
3. Learn what reviewer-visible weaknesses make a DTA paper look trivial.
4. Learn what counts as a mechanism-driven contribution versus a generic capacity increase.
5. Learn what minimum comparisons and ablations are needed for a credible paper.

Required outputs:
- reports/learning_review.md
- reports/cold_start_failure_modes.md
- reports/innovation_criteria.md
- reports/minimum_comparison_requirements.md

Requirements:
- Prefer 2025-2026 whenever possible.
- If older work must be mentioned for context, mark it explicitly as historical only.
- Record year and relevance for every important literature item.
- Be critical and publication-oriented.

Do not start implementation in Phase 0.

=============================
PHASE 1: INNOVATION SELECTION
=============================

Based on Phase 0 learning, design exactly one coherent research storyline.

User-provided candidate ideas:
1. drug graph perturbation + distillation
2. optimal transport
3. self-driven innovation after learning recent papers

Main storyline requirement:
All selected innovations must belong to one causal story, not unrelated tricks.

Evaluate whether the strongest storyline is:
- improving cold-drug generalization by making drug-side representations more stable and better aligned under perturbation

Select exactly:
- one main storyline
- two core innovations
- one incremental innovation

Guidance:
- Graph perturbation + distillation is a strong candidate for a core innovation if it directly targets cold-drug instability.
- If optimal transport is used, prefer it as an alignment regularizer between clean and perturbed drug representations, not as a flashy fusion-layer replacement, unless there is very strong evidence otherwise.
- The incremental innovation should be lightweight, easy to ablate, and clearly subordinate to the same storyline.

Required outputs:
- reports/storyline_design.md
- reports/innovation_selection_final.md
- reports/required_controls_for_storyline.md

Do not implement yet until the storyline is selected.

=============================================
PHASE 2: BASELINE REPRODUCTION AND RUNTIME FIX
=============================================

Current known issue:
placeholder runtime does not count as real evidence.

Your top priority is to convert the current scaffold into a real runnable baseline pipeline.

Tasks:
1. identify the exact blocker preventing real execution
2. list the minimum missing code/data/runtime pieces
3. implement only the minimum necessary fixes
4. run a real baseline smoke test
5. run a real baseline pilot experiment on the primary split
6. document all artifacts, configs, seeds, and outputs

Required outputs:
- reports/runtime_blocker_analysis.md
- reports/runtime_unblock_plan.md
- reports/reproduction_run_02.md
- reports/research_log.md updated

Rules:
- No more manuscript polishing before real execution works.
- If data is missing, specify exactly what data artifact is missing.
- If code is missing, specify exactly what module/function is missing.
- Only real executable runs count.

=================================
PHASE 3: IMPLEMENT THE INNOVATION
=================================

Only after the baseline is truly runnable:
1. implement the selected storyline
2. keep the diff minimal
3. keep the method lightweight
4. preserve fairness across compared methods

You must not implement unrelated add-ons.
Only implement:
- the two selected core innovations
- the one selected incremental innovation
- and nothing else unless required for execution

===========================================
PHASE 4: COMPARISON EXPERIMENTS + ABLATIONS
===========================================

Define and execute the minimum publishable experiment matrix.

Mandatory experiments:
1. baseline
2. baseline + core innovation 1
3. baseline + core innovation 1 + core innovation 2
4. full method
5. a decisive control against generic capacity increase if needed
6. full method with the core mechanism removed
7. at most one additional targeted ablation only if truly necessary

Evaluation rules:
- Davis and KIBA only
- cold-start only
- primary split: cold-drug
- secondary split: cold-target
- cold-both only if feasible
- same split files
- same preprocessing
- same seed policy
- same training budget
- same optimizer family unless strictly required otherwise
- same validation rule
- same early stopping logic

Seed policy:
- pilot runs: [2025, 2026, 2027]
- final runs if promising: [2025, 2026, 2027, 2028, 2029]

Reporting rules:
- report per-seed values
- report mean ± std
- record config path, split path, seed, git commit hash, runtime notes, and output artifact paths
- clearly label pilot vs final

Required outputs:
- reports/comparison_experiment_plan.md
- reports/experiment_matrix_final.md
- reports/ablation_plan.md
- reports/ablation_results.md
- reports/reproducibility_audit.md
- reports/research_log.md updated

================================
PHASE 5: MANUSCRIPT DRAFTING
================================

Only after the above phases are complete enough, write:
- drafts/paper_v0.md

The manuscript must read like a serious DTA paper, not a generic ML report.

Writing requirements:
1. One narrow main claim only.
2. Emphasize cold-start generalization, not random split.
3. Explain why the selected baseline family is relevant and where it fails.
4. Explain the selected mechanism in terms of cold-start failure mode, not generic feature enhancement.
5. Be explicit about fairness, seed control, reproducibility, split definitions, and evaluation scope.
6. Small gains must be described as modest but consistent.
7. If evidence is incomplete, mark it preliminary and list missing experiments.
8. Do not oversell novelty.
9. End with direct limitations and next experiments.

Required manuscript structure:
1. Title
2. Abstract
3. Introduction
4. Problem definition and cold-start setting
5. Related methods and baseline setting
6. Method
7. Experimental protocol
8. Main results
9. Ablations and robustness
10. Limitations
11. Conclusion

================================
STOPPING RULE
================================

Do not stop after planning or drafting alone.

Stop only when one of the following is true:
1. drafts/paper_v0.md is written and supported by the strongest real evidence currently feasible, OR
2. a concrete blocker prevents further real experimental progress, and all non-blocked work has still been completed.

Before stopping, ensure these are updated:
- reports/research_log.md
- reports/learning_review.md
- reports/cold_start_failure_modes.md
- reports/innovation_criteria.md
- reports/minimum_comparison_requirements.md
- reports/storyline_design.md
- reports/innovation_selection_final.md
- reports/required_controls_for_storyline.md
- reports/runtime_blocker_analysis.md
- reports/runtime_unblock_plan.md
- reports/comparison_experiment_plan.md
- reports/experiment_matrix_final.md
- reports/ablation_results.md
- reports/reproducibility_audit.md
- drafts/paper_v0.md

Final requirement:
At every stage, think critically, reject trivial ideas, and prefer a mechanism-driven storyline over the easiest implementation.
```

---

## 2. 学习优先版：强制先学 2024–2026，再决定创新

```text
Continue in this same cloud thread.
Do not create a PR yet.

From now on, switch to a learn-first workflow.
Do not implement any new method, do not modify model architecture, and do not continue manuscript polishing until the learning phase is complete.

We will use three gated phases:

Phase 0: Learning
Phase 1: Innovation selection
Phase 2: Implementation and experiments

Current instruction: execute Phase 0 only.

Phase 0 goals:
1. Study how recent DTA papers are actually framed and evaluated.
2. Study how cold-start settings are defined on Davis and KIBA.
3. Study what counts as a meaningful contribution versus a trivial capacity increase.
4. Study what comparison experiments and ablations are expected in a credible DTA manuscript.
5. Study whether recent lightweight baselines use mechanisms that are specifically relevant to cold-start generalization.

Required outputs:
- reports/learning_review.md
- reports/cold_start_failure_modes.md
- reports/innovation_criteria.md
- reports/minimum_comparison_requirements.md

Requirements for reports/learning_review.md:
Organize the literature and code audit into:
1. task setting
2. dataset and preprocessing conventions
3. split conventions
4. seed and fairness conventions
5. baseline families
6. common paper-story structures
7. common weak-paper patterns
8. what reviewers would likely reject

Requirements for reports/cold_start_failure_modes.md:
Identify the most plausible failure modes for:
- cold-drug
- cold-target
- cold-both

Requirements for reports/innovation_criteria.md:
Define what a publishable innovation for this project must satisfy.
It must explicitly distinguish:
- mechanism-driven ideas
- generic capacity-increase ideas
- ideas that are too trivial
- ideas that are lightweight but defensible

Requirements for reports/minimum_comparison_requirements.md:
Define the minimum comparison and ablation set needed so the paper does not look weak.

Hard rules:
- Do not implement new model changes in Phase 0.
- Do not propose generic MLP/gating/attention additions unless you can prove they target a specific cold-start failure mode.
- Do not invent claims, citations, or results.
- Be critical and publication-oriented.

Stopping rule for Phase 0:
Stop after the four reports above are complete and the research_log is updated with:
- what was learned
- what is still uncertain
- what the top 3 non-trivial innovation directions are
- what the single most convincing next step is

Do not start Phase 1 until Phase 0 is complete.
```

---

## 3. 年份约束补丁：只学 2024–2026

```text
Continue in this same cloud thread.
Do not create a PR yet.

Additional literature scope constraint for Phase 0:

From now on, restrict the learning phase to papers from 2024, 2025, and 2026 only.
Do not rely on older papers as primary learning material, primary baselines, or primary methodological inspiration unless they are absolutely unavoidable for historical context.

Rules:
1. Prioritize 2024-2026 papers only.
2. Prefer 2025-2026 whenever possible.
3. Older papers may be mentioned only briefly as historical background, not as the main basis for innovation selection.
4. If an older method is still used as an engineering baseline, explicitly state that it is old and justify why it is still included.
5. Every literature summary in Phase 0 must record the year and explain why the paper is relevant to cold-start Davis/KIBA DTA.
6. If no suitable 2024-2026 paper exists for a subtopic, explicitly say so instead of silently using older work.

Update the following outputs accordingly:
- reports/learning_review.md
- reports/cold_start_failure_modes.md
- reports/innovation_criteria.md
- reports/minimum_comparison_requirements.md

Do not start Phase 1 until this 2024-2026 constrained learning review is complete.
```

可选加强句：

```text
Any pre-2024 method must not be treated as the main publication anchor unless you explicitly justify why no suitable 2024-2026 lightweight alternative exists.
```

---

## 4. 创新审计版：防止它偷偷做成“加个 MLP”

```text
Continue in this same cloud thread.
Do not create a PR yet.

I am concerned that the current proposed method may be a trivial capacity-increase change, such as just adding an MLP, gate, attention block, or generic fusion head.

Before any further implementation or manuscript writing, critically audit the current proposed idea.

Write reports/innovation_audit.md and answer:

1. What exactly is the current proposed innovation?
2. Is it fundamentally more than a generic capacity increase?
3. Does it directly target a specific cold-start failure mechanism for unseen drugs or unseen targets?
4. What is the causal hypothesis behind it in one sentence?
5. If the same parameter budget were given to a plain MLP head, would the proposed method still be meaningfully different?
6. What is the minimum decisive ablation needed to prove the gain is not just from more parameters?
7. What is the strongest reviewer criticism against this idea?
8. Should this idea be rejected as too trivial?

Then define a required control experiment:
- baseline
- baseline + proposed method
- baseline + parameter-matched plain MLP control
- proposed method with the core mechanism removed

If the current idea is too trivial, reject it and propose exactly 3 better lightweight alternatives that are specifically designed for cold-start generalization rather than generic capacity increase.

For each alternative, provide:
- cold-start failure mode it targets
- mechanism hypothesis
- minimal implementation plan
- why it is stronger than adding an MLP
- decisive ablation
- expected publication value
- engineering cost

Do not implement anything new until this audit is complete.
Do not invent claims or results.
```

可选禁区约束：

```text
From now on, do not propose any innovation whose main effect could plausibly be explained as:
- more hidden layers
- more parameters
- more generic feature fusion
- a generic attention/gating block without a cold-start-specific mechanism

Every proposed idea must explicitly state why it targets cold-start generalization rather than generic capacity increase.
```

---

## 5. 主线重设计版：把多个想法压成一条主线

适用于你已经提出：
- 药物图扰动 + 蒸馏
- 最优传输
- 让它先学习别人怎么创新再自己创新

```text
Continue in this same cloud thread.
Do not create a PR yet.

We are redesigning the research direction.
From now on, use a learn-first, mechanism-first workflow.

Project scope is fixed:
- Task: drug-target affinity prediction
- Datasets: Davis and KIBA only
- Main setting: cold-start only
- Primary setting: cold-drug
- Secondary setting: cold-target
- Literature scope: 2024-2026 only
- Research goal: one single storyline, two core innovations, one incremental innovation

Candidate ideas provided by the user:
1. drug graph perturbation + distillation
2. optimal transport
3. learn how recent papers innovate, then design a stronger innovation

Critical constraint:
All innovations must belong to ONE causal storyline.
Do not build a paper around unrelated tricks.

Main storyline hypothesis to evaluate:
improving cold-drug generalization by making drug-side representations more stable and better aligned under perturbation.

Required learning task:
Study 2024-2026 DTA papers and closely related recent ML papers only.
Focus on:
- how recent papers frame innovation
- what counts as mechanism-driven innovation
- what looks like trivial module stitching
- what experimental evidence is expected
- how cold-start generalization is justified
- how strong papers organize main results and ablations

Required outputs:
1. reports/innovation_learning_2024_2026.md
2. reports/storyline_design.md
3. reports/innovation_selection_final.md
4. reports/required_controls_for_storyline.md

For reports/innovation_learning_2024_2026.md:
Organize what you learn into:
- innovation patterns that are actually publishable
- weak patterns that look like generic module swapping
- common reviewer criticisms
- how recent papers justify their novelty
- what makes a lightweight idea still defensible

For reports/storyline_design.md:
Evaluate whether the user’s 3 candidate ideas can be unified into one coherent storyline.
You must explicitly answer:
1. what is the single failure mode being targeted?
2. can graph perturbation + distillation be the first core innovation?
3. can optimal transport be used without becoming a generic fusion replacement?
4. if OT is used, should it be:
   - a fusion replacement, or
   - an alignment regularizer between clean and perturbed drug representations?
5. what should be the single incremental innovation?
6. what storyline is strongest for a credible paper?

Important rule:
Do NOT use optimal transport as a flashy replacement for a coarse fusion layer unless you can prove it is central to the same cold-start failure mechanism.
Prefer OT as a regularization/alignment mechanism rather than a generic architecture swap.

For reports/innovation_selection_final.md:
Select exactly:
- one main storyline
- two core innovations
- one incremental innovation

The selected design must satisfy:
- all parts belong to the same causal story
- not explainable as just more parameters
- directly target cold-drug generalization
- easy to ablate
- lightweight enough to implement
- stronger than adding an MLP / gate / generic attention block
```

---

## 6. 运行解堵版：先把 placeholder runtime 变成真实运行

```text
Continue in this same cloud thread.
Do not create a PR yet.

The current Phase 2 setup is not sufficient.
The highest priority is no longer planning, schema design, or manuscript drafting.
The highest priority is to remove the placeholder runtime blocker and obtain real executable training/evaluation runs.

Immediate objective:
convert the current placeholder runtime into a real runnable baseline pipeline for Davis/KIBA cold-start experiments.

Tasks:
1. identify exactly why runtime is still placeholder
2. list the minimum missing code/data/runtime pieces required for real execution
3. implement only the minimum necessary fixes
4. run a real baseline smoke test
5. run a real baseline pilot experiment on the primary split
6. if and only if the baseline pilot runs successfully, run the matched innovation pilot
7. update all affected reports accordingly

Required outputs:
- reports/runtime_blocker_analysis.md
- reports/runtime_unblock_plan.md
- reports/reproduction_run_02.md
- reports/research_log.md updated

Rules:
- no more manuscript polishing before real execution works
- no invented metrics
- no placeholder claims treated as evidence
- if data is missing, explicitly state what exact dataset artifact is missing
- if code is missing, explicitly state which module/function is missing
- if training is still not runnable, stop only after producing a precise blocker report and the minimal patch set needed next
```

可选加强句：

```text
A placeholder pilot run does not count as experimental evidence.
Do not treat pipeline integrity alone as progress toward the main result table.
Only real executable baseline and innovation runs count.
```

---

## 7. 对比实验优先版：先证据，后写作

```text
Continue in this same cloud thread.
Do not create a PR yet.

Paper quality now depends on strong comparative evidence.
Before further manuscript writing, prioritize comparison experiments.

I need a publication-quality comparison plan and execution.

Write reports/comparison_experiment_plan.md and then execute the highest-priority runs.

Requirements:
1. Define the minimum comparison set needed for a credible paper.
2. Separate:
   - engineering baseline
   - publication comparison baseline(s)
   - proposed method
3. Use exactly the same:
   - dataset version
   - preprocessing
   - split files
   - seed list
   - optimizer family
   - early stopping rule
   - max epoch budget
   - validation rule
4. Main setting must be cold-start only.
5. Random split must not be the main result.
6. Use one primary split and one secondary split.
7. Pilot runs use 3 seeds: [2025, 2026, 2027]
8. Final runs use 5 seeds: [2025, 2026, 2027, 2028, 2029] only if pilot is promising.

The output must include:
- the exact comparison matrix
- what will be run first
- what counts as a fair comparison
- what would make the paper story weak
- what would make the paper story credible

Then execute the smallest valid comparison runs.
Update:
- reports/comparison_experiment_plan.md
- reports/research_log.md
- reports/required_tables.md
- drafts/paper_v0.md only after real comparison evidence exists

Do not invent numbers.
Do not overclaim.
```

---

## 8. 最小可发表实验矩阵版

```text
Continue in this same cloud thread.
Do not create a PR yet.

Define and execute the minimum publishable experiment matrix.

Mandatory matrix:
1. Main comparison:
   - baseline
   - proposed method
   on Davis and KIBA under the primary cold-start split

2. Secondary comparison:
   - baseline
   - proposed method
   on Davis and KIBA under the secondary cold-start split

3. Mandatory ablation:
   - baseline
   - baseline + proposed idea
   - proposed idea with the new component removed
   - at most one additional targeted ablation only if necessary

4. Seed protocol:
   - pilot: [2025, 2026, 2027]
   - final if promising: [2025, 2026, 2027, 2028, 2029]

5. Reporting protocol:
   - per-seed values
   - mean +- std
   - same preprocessing, split files, training budget, validation rule, and early stopping across all compared methods

Write the matrix to reports/experiment_matrix_final.md and begin execution in priority order.
Update reports/research_log.md continuously.
Do not invent numbers.
```

---

## 9. 论文质量提升版：按审稿人逻辑改稿

```text
Continue in this same cloud thread.
Do not create a PR yet.

Improve the manuscript quality by revising the paper around evidence, not around wording.

Revise drafts/paper_v0.md with the following quality rules:

1. The paper must make one narrow main claim only:
   a minimal modification improves cold-start generalization under a fair protocol.

2. The Introduction must clearly answer:
   - why DTA matters,
   - why cold-start is the real setting of interest,
   - why existing lightweight baselines are still insufficient,
   - why our contribution is small but defensible.

3. The Method section must avoid vague novelty language.
   It must explicitly say:
   - what exact component changed,
   - why it should help cold-start,
   - why it is minimal,
   - why it is easy to ablate.

4. The Experimental Protocol section must be unusually explicit:
   - Davis/KIBA version
   - preprocessing
   - split definition
   - seed policy
   - fairness constraints
   - logging rules

5. The Results section must prioritize:
   - main comparison table
   - ablation table
   - robustness / reproducibility notes
   - only then any optional analysis

6. If gains are small, describe them as modest but consistent.
7. If evidence is incomplete, label it preliminary.
8. Do not write broad SOTA-style claims.
9. End with honest limitations and the next essential experiment.

Do not invent numbers or citations.
Use repository evidence only.
```

---

## 10. 审稿人自查版：让它自己挑错

```text
Continue in this same cloud thread.
Do not create a PR yet.

Audit the current manuscript and experiment plan like a strict reviewer.

Write reports/reviewer_style_self_critique.md.

The critique must identify:
1. where the novelty may look weak,
2. where the protocol may look unfair,
3. where the comparison set may look outdated,
4. where the ablation may be insufficient,
5. where the writing may overclaim,
6. what the single highest-value missing experiment is,
7. what must be fixed before the manuscript looks credible.

Be critical, specific, and conservative.
```

---

## 11. 过夜续跑版：让它不中途停

```text
Continue in this same cloud thread.
Do not create a PR yet.
Treat my previous prompts as one continuous research pipeline and execute them in order.

Do not wait for further confirmation between steps.

Execution rule:
1. Continue through the remaining steps autonomously.
2. If one step is blocked, continue with any other non-blocked steps.
3. Keep updating reports/research_log.md with progress, blockers, and completed outputs.
4. Stop only when either:
   - drafts/paper_v0.md is written, or
   - you hit a concrete blocker that prevents a credible draft.

Do not invent results, numbers, or citations.
Use only evidence available from the repository, generated reports, actual runs, and verified baseline scouting.
```

如果希望它不要把“有初稿”当结束，可改成：

```text
Do not treat a draft manuscript as task completion.
A draft without real comparison evidence is not considered sufficient completion.
```

---

## 推荐使用顺序

### 路线 A：从头开始
1. `学习优先版`
2. `年份约束补丁`
3. `主线重设计版`
4. `运行解堵版`
5. `对比实验优先版`
6. `最小可发表实验矩阵版`
7. `论文质量提升版`
8. `审稿人自查版`

### 路线 B：已经在跑，只想总控
1. `总控版`
2. 如果发现 runtime 还是假跑，再发 `运行解堵版`
3. 如果发现创新太水，再发 `创新审计版`
4. 如果发现只会写文档不跑实验，再发 `对比实验优先版`

---

## 最后提醒

最容易让 Codex 跑偏的 4 件事：

1. **停止条件写成“出初稿就停”**
2. **没有强制 parameter-matched control**
3. **没有写死 cold-start 是主结果**
4. **没有把创新和 failure mode 绑定**

所以最关键的一句永远是：

> Every proposed innovation must explicitly state why it targets cold-start generalization rather than generic capacity increase.

