import json
import datetime

def update_jsonl(filepath, agent, delta):
    with open(filepath, 'a') as f:
        entry = {
            "agent": agent,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "knowledge_delta": delta
        }
        f.write(json.dumps(entry) + '\n')

update_jsonl('/home/blablabla/agent-forge/agents/vetinari/local_knowledge.jsonl', '@vetinari', 'Initiated OSINT investigation on Tomasz Radkiewicz. Mapped affiliations: PIFS, Trakt. Designed 3-loop investigation plan focusing on KRS/CEIDG, passive DNS, and HUMINT transcription.')
update_jsonl('/home/blablabla/agent-forge/agents/elliot/local_knowledge.jsonl', 'elliot', 'Drafted technical execution matrix for Radkiewicz OSINT. Configured passive collection (theHarvester, spiderfoot) and HUMINT archival (yt-dlp, Whisper) routing through Mullvad.')
