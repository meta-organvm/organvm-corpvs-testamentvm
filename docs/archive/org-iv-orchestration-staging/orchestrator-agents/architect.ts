import { ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { GoogleGenerativeAIEmbeddings } from "@langchain/google-genai";
import { Chroma } from "@langchain/community/vectorstores/chroma";
import { Document } from "@langchain/core/documents";

export class ArchitectService {
  private model: ChatGoogleGenerativeAI;
  private embeddings: GoogleGenerativeAIEmbeddings;
  private vectorStore: Chroma | null = null;
  private initialized = false;

  constructor() {
    const apiKey = process.env.GEMINI_API_KEY; // allow-secret
    if (!apiKey) console.warn("⚠️ Architect: GEMINI_API_KEY missing. I am blind.");

    this.model = new ChatGoogleGenerativeAI({
      modelName: "gemini-2.5-flash", // Using the latest
      apiKey: apiKey, // allow-secret
      maxOutputTokens: 2048,
    });

    this.embeddings = new GoogleGenerativeAIEmbeddings({
      modelName: "embedding-001",
      apiKey: apiKey, // allow-secret
    });
  }

  async init() {
    if (this.initialized) return;
    
    try {
      // Connect to Chroma Container
      this.vectorStore = new Chroma(this.embeddings, {
        url: process.env.CHROMA_URL || "http://chroma:8000",
        collectionName: "omni-universe",
      });
      
      console.log("🧠 Architect: Connected to Deep Memory (ChromaDB).");
      this.initialized = true;
    } catch (e) {
      console.error("❌ Architect: Failed to connect to Memory.", e);
    }
  }

  /**
   * Embeds a document into the system's long-term memory.
   */
  async memorize(content: string, metadata: Record<string, any>) {
    if (!this.vectorStore) return;
    
    const doc = new Document({
      pageContent: content,
      metadata: metadata,
    });

    await this.vectorStore.addDocuments([doc]);
    console.log(`💾 Architect: Memorized ${metadata.source}`);
  }

  /**
   * Semantic Search + Reasoning
   */
  async ask(question: string): Promise<string> {
    if (!this.vectorStore) return "I have no memory.";

    // 1. Retrieval
    const results = await this.vectorStore.similaritySearch(question, 5);
    const context = results.map(r => 
      `SOURCE: ${r.metadata.source}\nCONTENT: ${r.pageContent}`
    ).join("\n\n");

    // 2. Generation (Direct invoke for now, can upgrade to Chain)
    const prompt = `You are the Architect of the Omni-Dromenon. 
    Answer the question based on the context.
    
    CONTEXT:
    ${context}
    
    QUESTION:
    ${question}`;

    const response = await this.model.invoke(prompt);
    // LangChain response content can be string or array. Cast safely.
    return response.content.toString();
  }
}

export const architect = new ArchitectService();
