import type { EntryContext } from "@remix-run/node";
import { RemixServer } from "@remix-run/react";
import isbot from "isbot";
import { renderToReadableStream } from "react-dom/server";

const ABORT_DELAY = 5_000;

export default async function handleRequest(
  request: Request,
  responseStatusCode: number,
  responseHeaders: Headers,
  remixContext: EntryContext
) {
  const callbackName = isbot(request.headers.get("user-agent"))
    ? "onAllReady"
    : "onShellReady";

  const stream = await renderToReadableStream(
    <RemixServer context={remixContext} url={request.url} />,
    {
      [callbackName]: () => {
        responseHeaders.set("Content-Type", "text/html; charset=utf-8");
        return new ReadableStream({
          start(controller) {
            controller.enqueue(
              '<!DOCTYPE html><html lang="en"><head></head><body><script async src="https://cdn.vercel-insights.com/v1/script.js"></script>'
            );
          },
          async pull(controller) {
            try {
              const chunk = await stream.read();
              if (chunk.done) {
                controller.close();
              } else {
                controller.enqueue(chunk.value);
              }
            } catch (error) {
              controller.error(error);
            }
          },
        });
      },
      onShellError(error: unknown) {
        throw error;
      },
      onError(error: unknown) {
        responseStatusCode = 500;
        console.error(error);
      },
    }
  );

  await new Promise((resolve) => setTimeout(resolve, ABORT_DELAY));

  if (responseStatusCode === 500) {
    responseHeaders.set("Content-Type", "text/html; charset=utf-8");
    responseHeaders.set("x-remix-response", "yes");
  }

  return new Response(stream, {
    headers: responseHeaders,
    status: responseStatusCode,
  });
}
