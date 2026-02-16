import { systemBus } from '../bus/system-bus.js';
import { MetasystemEvent } from '../types/metasystem.js';
import { LLMClient } from '../dreamcatcher/llm-client.js';

export class CriticAgent {
  private llm: LLMClient;

  constructor() {
    this.llm = new LLMClient();
  }

  async start() {
    console.log('🧐 Critic Agent Activated');
    await systemBus.subscribe(async (event: MetasystemEvent) => {
      if (event.type === 'repo.pull_request') {
        await this.reviewPullRequest(event);
      }
    });
  }

  private async reviewPullRequest(event: MetasystemEvent) {
    const { action, pull_request, repository } = event.payload;

    if (action !== 'opened' && action !== 'synchronize') return;

    console.log(`🔍 [Critic] Reviewing PR: ${repository.full_name} #${pull_request.number}`);

    // In a real scenario, we would fetch the diff here. 
    // For this prototype, we simulate the logic.
    const systemPrompt = `You are the Metasystem Critic. Your job is to review Pull Requests for alignment with the Sovereign Architecture.
    Project: ${repository.full_name}
    PR: ${pull_request.title}
    
    CRITERIA:
    1. Must respect the seed.yaml constraints.
    2. Must be professional and concise.
    3. If it looks like commercial logic in the Alchemist org (ivviiviivvi), FLAG IT for migration to the Guild (labores-profani-crux).`;

    const userPrompt = `Review this PR: ${pull_request.title}\n\nDescription: ${pull_request.body}`;

    try {
      const response = await this.llm.callGemini('gemini-1.5-flash-latest', systemPrompt, userPrompt);
      console.log(`✅ [Critic] Review Complete for #${pull_request.number}`);
      
      // In production, we would call GitHub API to post the comment:
      // await postGitHubComment(repository.full_name, pull_request.number, response.content);
      
      console.log('--- REVIEW START ---');
      console.log(response.content);
      console.log('--- REVIEW END ---');
      
    } catch (err) {
      console.error('❌ [Critic] Review Failed:', err);
    }
  }
}

export const criticAgent = new CriticAgent();
