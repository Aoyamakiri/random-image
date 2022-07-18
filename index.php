<?php

use Hyperf\Nano\Factory\AppFactory;
use Hyperf\HttpMessage\Stream\SwooleStream;
use Dotenv\Dotenv;

require_once __DIR__ . '/vendor/autoload.php';

$dotenv = Dotenv::createUnsafeImmutable(__DIR__);
$dotenv->load();

$appConfig = [
    'host' => env('APP_HOST', '0.0.0.0'),
    'port' => (int)env('APP_PORT', 9501),
];

$imageConfig = [
    'max' => (int)env('MAX_IMAGES', 0),
];

$app = AppFactory::create(...$appConfig);

$app->get('/', function () use ($imageConfig) {
    if ($imageConfig['max'] === 0) {
        return $this->response->json(['message' => 'You must need some images.']);
    }

    $image = BASE_PATH . '/images/' . mt_rand(0, $imageConfig['max']) . '.webp';
    $imageContent = file_get_contents($image);

    return $this->response
        ->withHeaders([
            'Access-Control-Allow-Origin' => '*',
            'Content-Type' => 'webp',
        ])
        ->withBody(new SwooleStream($imageContent));
});

$app->run();
